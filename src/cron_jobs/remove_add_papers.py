import os
import pandas as pd

def remove_old_papers(data_path, save_path) -> None:
    """Remove all the papers from the oldest day"""
    df = pd.read_json(path_or_buf=data_path, lines=True)
    df["published_date"] =  pd.to_datetime(arg=df['published_date'])
    oldest_date =  df['published_date'].min().date() 
    papers_to_remove = df[df['published_date'].dt.date == oldest_date]
    df = df[~df.index.isin(values=papers_to_remove.index)]
    df.to_json(path_or_buf=save_path, orient="records", lines=True)

def add_new_papers(latest_papers_path, master_data_path) -> None:
    """Add new papers to the master data JSON file"""
    latest_papers = pd.read_pickle(filepath_or_buffer=latest_papers_path)

    # Check if the master data file already exists
    if os.path.exists(path=master_data_path):
        master_data = pd.read_json(path_or_buf=master_data_path, lines=True)
        # Concatenate the latest papers DataFrame with the existing master data
        master_data = pd.concat(objs=[master_data, latest_papers], ignore_index=True)
    else:
        # If the master data file doesn't exist, use the latest papers as the master data
        master_data = latest_papers
    master_data.to_json(path_or_buf=master_data_path, orient="records", lines=True)

remove_old_papers(data_path="../../data/master_data.json", save_path="../../data/master_data.json")
add_new_papers(latest_papers_path="../../data/latest_papers.pkl", master_data_path="../../data/master_data.json")

