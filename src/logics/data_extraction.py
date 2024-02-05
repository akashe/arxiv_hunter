import os.path
from tqdm import tqdm
import argparse

import requests
import feedparser
import pandas as pd
from datetime import datetime, timedelta
import fitz  # this is pymupdf
from typing import Dict, List, Tuple

STANDARD_SEARCH_QUERY = "cat:cs.CV OR cat:cs.AI OR cat:cs.LG OR cat:cs.CL OR cat:cs.NE OR cat:stat.ML OR cat:cs.IR"


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

        downloaded_data: Dict[str, Dict[str, str]] = {}

        # Loop through the entries
        for entry in tqdm(entries):
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
                    "title": title,
                    "published_date": published_date,
                    "pdf_link": pdf_link,
                    "summary": summary,
                    "pdf_text": pdf_text,
                }
        # Convert the extracted data into a pandas dataframe
        df = pd.DataFrame.from_dict(downloaded_data, orient="index")
        return df

    def store_data(
        self,
        save_file_name: str = "master_data.pkl",
        max_results: int = 10,
        days: int = 60,
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
        default=50,
    )
    parser.add_argument(
        "-d",
        "--days",
        type=str,
        help="Store only for these many past days",
        nargs="?",
        default=50,
    )

    # Parse the arguments
    args = parser.parse_args()

    max_results = args.max_results
    days = args.days

    # initialize parser
    parser = ArxivParser()

    # store the past data
    parser.store_data(max_results=max_results, days=days)