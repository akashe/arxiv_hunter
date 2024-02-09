"""This module contains the ArxivSearcher class that takes a query string from the user and returns the data from the arxiv API in JSON format."""
from abc import ABC, abstractmethod
import os
from typing import Dict, List
import json
from datetime import datetime
import requests
from tqdm import tqdm
import feedparser

class ArxivSearcher(ABC):
    STANDARD_SEARCH_QUERY: str = ("cat:cs.CV OR cat:cs.AI OR cat:cs.LG OR cat:cs.CL OR cat:cs.NE OR cat:stat.ML OR cat:cs.IR")
    BASE_URL = "http://export.arxiv.org/api/query"

    def __init__(self) -> None:
        super().__init__()
        print("...ArxivSearcher initialized...")

    def search(self, query:str, days:int, max_results:int):
        self.days = days
        params = {
            "search_query": str(query) + self.STANDARD_SEARCH_QUERY,
            "start": 0,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }

        url = self.BASE_URL + "?" + requests.compat.urlencode(params)
        print(f"SEARCH URL: {url}")
        response = requests.get(url, timeout=15)
        
        entries = feedparser.parse(response.text).entries

        downloaded_data: List[Dict[str, str]] = []

       
        for entry in tqdm(entries):
            published_date = datetime.strptime(entry.published, "%Y-%m-%dT%H:%M:%SZ")
            current_date = datetime.now()
            date_diff = (current_date - published_date).days

           
            if date_diff <= days:
                link = entry.link
                pdf_link = link.replace("abs", "pdf")
                downloaded_data.append(
                    {
                        "id": entry.id,
                        "title": entry.title,
                        "published_date": str(published_date),
                        "pdf_link": pdf_link,
                        "summary": entry.summary,
                    }
                )
        
        downloaded_data.extend(downloaded_data)
        
        return json.dumps(downloaded_data)

    

if __name__=="__main__":
    arxiv_parser = ArxivSearcher()
    res = arxiv_parser.search(
        query="attention mechanism, llm",
        days=60,
        max_results=5
    )
    print(res)