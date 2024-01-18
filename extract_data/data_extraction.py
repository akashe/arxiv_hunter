import requests
import feedparser
import pandas as pd
from datetime import datetime, timedelta
import fitz # this is pymupdf
from typing import Dict, List, Tuple

class ArxivParser:
    base_url = "http://export.arxiv.org/api/query"
    def __init__(self):
        EntryData = Dict[str, str]
        self.extracted_data: Dict[str, EntryData] = {}
        
    def get_results(self, max_results: int = 5, days: int = 60) -> pd.DataFrame:
        # Construct the url with the query parameters
        params = {
            "search_query": f"cat:cs*",
            "start": 0,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending"
        }
        url = self.base_url + "?" + requests.compat.urlencode(params)

        # Send a GET request to the api endpoint
        response = requests.get(url)
        # Parse the response
        entries = feedparser.parse(response.text).entries
        
        # Loop through the entries
        for entry in entries:
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
                self.extracted_data[id] = {
                    "title": title,
                    "published_date": published_date,
                    "pdf_link": pdf_link,
                    "summary": summary,
                    "pdf_text": pdf_text
                }
        # Convert the extracted data into a pandas dataframe
        df = pd.DataFrame.from_dict(self.extracted_data, orient="index")
        return df
        
    def store_data(self, max_results: int = 10, days: int = 60) -> None:
        # Call the get_results method and store the dataframe in the self.extracted_data attribute
        self.extracted_data = self.get_results(max_results, days)
        
        # Feature Engineer two new columns
        self.extracted_data['summary_length'] = self.extracted_data.apply(lambda row: len(row['summary']), axis=1)
        self.extracted_data['pdf_text_length'] = self.extracted_data.apply(lambda row: len(row['pdf_text']), axis=1)
        self.extracted_data.to_pickle("master_data.pkl")

    def get_stored_data(self) -> pd.DataFrame:
        # Return the self.extracted_data attribute
        return self.extracted_data

class User:
    def __init__(self):
        self.master_data = pd.read_pickle('master_data.pkl')
        self.user_data = None # this will store the filtered dataframe
    
    def search(self, query):
        mask = self.master_data["pdf_text"].str.contains(query) # create a boolean mask
        self.user_data = self.master_data[mask] # filter the master_data using the mask
        return self.user_data
    
    def feed(self):
        return self.user_data.sort_values("published_date", ascending=False).head(2)

if __name__ == "__main__":
    user1=User()
    result=user1.search("llm")
    print(result)
    