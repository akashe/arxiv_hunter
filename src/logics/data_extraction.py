import os.path
import pdb

from tqdm import tqdm
import argparse
import multiprocessing

import requests
import feedparser
import pandas as pd
from datetime import datetime, timedelta
import fitz  # this is pymupdf
from typing import Dict, List, Tuple

STANDARD_SEARCH_QUERY = f"cat:cs.CV OR cat:cs.AI OR cat:cs.LG OR cat:cs.CL OR cat:cs.NE OR cat:stat.ML OR cat:cs.IR"


def download_data(local_entries, split_no, save_path, days):
    print("Downloading")
    downloaded_data: Dict[str, Dict[str, str]] = {}
    # Loop through the entries
    for entry in tqdm(local_entries):
        try:
            published_date = datetime.strptime(entry.published, "%Y-%m-%dT%H:%M:%SZ")
            current_date = datetime.now()
            date_diff = (current_date - published_date).days

            # Check if the date difference is less than or equal to the days parameter
            if date_diff <= days:
                id = entry.id
                title = entry.title
                link = entry.link
                summary = entry.summary

                # Get the pdf link by replacing the "abs" with "pdf" in the link
                pdf_link = link.replace("abs", "pdf")
                # Get the pdf content by sending a GET request to the pdf link and opening it with fitz
                pdf_content = requests.get(pdf_link).content
                pdf_file = fitz.open(stream=pdf_content, filetype="pdf")
                # Extract the text from the pdf file
                pdf_text = ""
                for page in pdf_file:
                    pdf_text += page.get_text()
                # Store the extracted data in the dictionary with the id as the key
                downloaded_data[id] = {
                    "id": id,
                    "title": title,
                    "published_date": published_date,
                    "pdf_link": pdf_link,
                    "summary": summary,
                    "pdf_text": pdf_text,
                }
        except Exception as e:
            print("Failed for an entry")
            print(e)
            continue
    # Convert the extracted data into a pandas dataframe
    save_location = os.path.join(save_path, f"split_{split_no}.pkl")
    pd.DataFrame.from_dict(downloaded_data, orient="index").to_pickle(save_location)


class ArxivParser:
    base_url = "http://export.arxiv.org/api/query"

    def __init__(self, data_path="data/"):
        self.extracted_data: pd.DataFrame = pd.DataFrame()

        if not os.path.exists(data_path):
            os.makedirs(data_path)
        self.data_path = data_path

    def get_results(
        self,
        max_results: int = 5,
        days: int = 60,
        search_query: str = STANDARD_SEARCH_QUERY,
        num_threads: int = 8,
    ) -> pd.DataFrame:
        # Construct the url with the query parameters
        params = {
            "search_query": search_query,
            "start": 0,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
        url = self.base_url + "?" + requests.compat.urlencode(params)

        # Send a GET request to the api endpoint
        response = requests.get(url)
        # Parse the response
        entries = feedparser.parse(response.text).entries

        splits = []
        for i in range(num_threads):
            splits.append(
                entries[
                    (i * (len(entries) // num_threads)) : (
                        (i + 1) * (len(entries) // num_threads)
                    )
                ]
            )

        if len(entries) % num_threads != 0:
            mod = len(entries) % num_threads
            splits[-1].extend(entries[-mod:])

        process_list = []
        for i, split in enumerate(splits):
            p = multiprocessing.Process(
                target=download_data, args=[split, i, self.data_path, days]
            )
            p.start()
            process_list.append(p)

        for process in process_list:
            process.join()

        dfs = []
        # combine all the downloaded content
        for i in range(len(splits)):
            save_path = os.path.join(self.data_path, f"split_{i}.pkl")
            df = pd.read_pickle(save_path)
            dfs.append(df)

        return pd.concat(dfs, ignore_index=True)

    def store_data(
        self,
        save_file_name: str = "master_data3.pkl",
        max_results: int = 500,
        days: int = 365*2,
    ) -> None:
        # Call the get_results method and store the dataframe in the self.extracted_data attribute
        self.extracted_data = self.get_results(max_results, days)

        assert len(self.extracted_data) > 0, "Got no results with the search query"
        # Feature Engineer two new columns
        self.extracted_data["summary_length"] = self.extracted_data.apply(
            lambda row: len(row["summary"]), axis=1
        )
        self.extracted_data["pdf_text_length"] = self.extracted_data.apply(
            lambda row: len(row["pdf_text"]), axis=1
        )

        save_location = os.path.join(self.data_path, save_file_name)
        self.extracted_data.to_pickle(save_location)

    def get_stored_data(self) -> pd.DataFrame:
        # Return the self.extracted_data attribute

        assert len(self.extracted_data) != 0, "Please store data first"
        return self.extracted_data


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="A recommender system based on tf-idf and cosine similarity"
    )

    # Add an argument for the query
    parser.add_argument(
        "-m",
        "--max_results",
        type=str,
        help="Maximum results to store",
        nargs="?",
        default=500,
    )
    parser.add_argument(
        "-d",
        "--days",
        type=str,
        help="Store only for these many past days",
        nargs="?",
        default=365*2,
    )

    # Parse the arguments
    args = parser.parse_args()

    max_results = args.max_results
    days = int(args.days)

    # initialize parser
    parser = ArxivParser()

    # store the past data
    parser.store_data(max_results=max_results, days=days)
