import requests
import feedparser
from datetime import datetime, timedelta
import fitz # this is pymupdf
from typing import Dict, List, Tuple

# Define the ArxivParser class
class ArxivParser:
    def __init__(self, query: str = "llm", max_results: int = 10, days: int = 60):
        self.query = query
        self.max_results = max_results
        self.days = days
        self.url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
        # Send a GET request to api endpoint
        self.response = requests.get(self.url)
        # Parse the response
        self.entries = feedparser.parse(self.response.text).entries
        # Use a type alias to define the type of the dictionary values
        EntryData = Dict[str, str]
        self.extracted_data: Dict[str, EntryData] = {}

    def store_entries(self) -> None:
        # Loop through the entries
        for entry in self.entries:
            published_date = datetime.strptime(entry.published, "%Y-%m-%dT%H:%M:%SZ")
            current_date = datetime.now()
            date_diff = (current_date - published_date).days
            # Check if the date difference is less than or equal to the days parameter
            if date_diff <= self.days:
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
                # Store the id as the key and the values in a nested dictionary
                self.extracted_data[id] = {"title": title, "published_date":published_date, "pdf_link": pdf_link, "summary": summary, "pdf_text": pdf_text}
            else:
                # Break the loop if the date difference is greater than the days parameter
                break

if __name__=="__main__":
    parser = ArxivParser()
    parser.store_entries()
    data=parser.extracted_data
    
    for article in data:
        print(f"Id: {article}")
        print(f"Published date: {data[article]['published_date']}")
        print(f"Pdf link: {data[article]['pdf_link']}\n")
        print(f"Title: {data[article]['title']}\n")
        print(f"Summary: {data[article]['summary']}\n")
        print(f"Content: {data[article]['pdf_text']}")
        break
