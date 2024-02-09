"""This module contains the ArxivParser class that extracts and parses 
    data from the arxiv API and stores it in a JSON file."""
from abc import ABC, abstractmethod
import os
from pathlib import Path
import json
from typing import Optional, List, Dict
import requests
from datetime import datetime
import feedparser
import fitz
from tqdm import tqdm
BASE_PATH = Path(__file__).resolve().parent
print(f"BASE_PATH: {BASE_PATH}")
class ArxivExtractorBase(ABC):
    """Class that extracts data from Arxiv-Api and Loads Data in Json"""

    @abstractmethod
    def extract_data(self):
        """Extract data from Arxiv-Api"""

    @abstractmethod
    def store_data(self):
        """Store data as Json File"""

class ArxivExtractor(ArxivExtractorBase):
    STANDARD_SEARCH_QUERY: str = ("cat:cs.CV OR cat:cs.AI OR cat:cs.LG OR cat:cs.CL OR cat:cs.NE OR cat:stat.ML OR cat:cs.IR")
    BASE_URL = "http://export.arxiv.org/api/query"

    def __init__(self, days:int, max_results:int=5, data_path:str="data/") -> None:
        self.days=days
        self.max_results=max_results
        if not os.path.exists(data_path):
            os.makedirs(data_path)
        self.data_path = data_path
        
        params = {
                "search_query": self.STANDARD_SEARCH_QUERY,
                "start": 0,
                "max_results": max_results,
                "sortBy": "submittedDate",
                "sortOrder": "descending",
            }
        self.URL = self.BASE_URL + "?" + requests.compat.urlencode(params)

    def extract_data(self):
        response = requests.get(self.URL, timeout=15)
        entries = feedparser.parse(response.text).entries
        downloaded_data: List[Dict[str, str]] = ([])
       
        for entry in tqdm(entries):
            published_date = datetime.strptime(entry.published, "%Y-%m-%dT%H:%M:%SZ")
            current_date = datetime.now()
            date_diff = (current_date - published_date).days

           
            if date_diff <= self.days:
                link = entry.link
                pdf_link = link.replace("abs", "pdf")
                pdf_content = requests.get(pdf_link, timeout=15).content
                pdf_file = fitz.open(stream=pdf_content, filetype="pdf")
                
                pdf_text = ""
                for page in pdf_file:
                    pdf_text += page.get_text()
                
                downloaded_data.append(
                    {
                        "id": entry.id,
                        "title": entry.title,
                        "summary": entry.summary,
                        "published_date": str(published_date),
                        "pdf_link": pdf_link,
                        "pdf_text": pdf_text,
                    }
                )
        print(f"DOWNLOADED DATA: {len(downloaded_data)}")
        return downloaded_data
    
    def store_data(self):
        extracted_data = self.extract_data()

        assert len(extracted_data) > 0, "Got no results with the search query"
        
        save_location = os.path.join(self.data_path, "master_data.json")
        with open(save_location, "w", encoding="utf-8") as f:
            json.dump(extracted_data, f, indent=4)
    
if __name__ == "__main__":
    import pandas as pd
    print ("Current working directory:")
    print (os.getcwd())
    arxiv_extractor = ArxivExtractor(days=60,max_results=5, data_path="data/")
    arxiv_extractor.store_data()
    