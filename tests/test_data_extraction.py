import pytest
from datetime import datetime, timedelta
from src.logics.data_extraction import ArxivParser

import pandas as pd


@pytest.fixture
def arxiv_parser():
    return ArxivParser()


# Test the get_results method with different parameters
def test_get_results(arxiv_par):
    # Test with max_results = 5 and days = 60
    df1 = arxiv_par.get_results(max_results=5, days=60)

    # Check that the dataframe has 5 rows and 5 columns
    assert df1.shape == (5, 5)
    assert list(df1.columns) == [
        "title",
        "published_date",
        "pdf_link",
        "summary",
        "pdf_text",
    ]

    # Check that the dataframe contains only entries from the last 60 days
    assert df1["published_date"].max() <= datetime.now()
    assert df1["published_date"].min() >= datetime.now() - timedelta(days=60)

    # Test with max_results = 10 and days = 30
    df2 = arxiv_parser.get_results(max_results=10, days=30)

    # Check that the dataframe has 10 rows and 5 columns
    assert df2.shape == (15, 5)

    # Check that the dataframe contains only entries from the last 30 days
    assert df2["published_date"].max() <= datetime.now()
    assert df2["published_date"].min() >= datetime.now() - timedelta(days=30)


# Test the store_data method with different parameters
def test_store_data(arxiv_par):
    # Test with max_results = 5 and days = 60
    arxiv_par.store_data(max_results=5, days=60)

    # Check that the extracted_data attribute is a pandas dataframe with 5 rows and 7 columns
    assert isinstance(arxiv_par.extracted_data, pd.DataFrame)
    assert arxiv_par.extracted_data.shape == (5, 7)
    assert list(arxiv_par.extracted_data.columns) == [
        "title",
        "published_date",
        "pdf_link",
        "summary",
        "pdf_text",
        "summary_length",
        "pdf_text_length",
    ]

    # Check that the dataframe contains only entries from the last 60 days
    assert arxiv_par.extracted_data["published_date"].max() <= datetime.now()

    assert arxiv_par.extracted_data[
        "published_date"
    ].min() >= datetime.now() - timedelta(days=60)

    # Check that the master_data.pkl file is created and contains the same data as the extracted_data attribute
    master_data = pd.read_pickle("master_data.pkl")
    assert master_data.equals(arxiv_par.extracted_data)

    # Test with max_results = 10 and days = 30
    arxiv_par.store_data(max_results=10, days=30)

    # Check that the extracted_data attribute is a pandas dataframe with 10 rows and 7 columns
    assert isinstance(arxiv_par.extracted_data, pd.DataFrame)
    assert arxiv_par.extracted_data.shape == (15, 7)

    # Check that the dataframe contains only entries from the last 30 days
    assert arxiv_par.extracted_data["published_date"].max() <= datetime.now()
    assert arxiv_par.extracted_data[
        "published_date"
    ].min() >= datetime.now() - timedelta(days=30)

    # Check that the master_data.pkl file is updated and contains the same data as the extracted_data attribute
    master_data = pd.read_pickle("master_data.pkl")
    assert master_data.equals(arxiv_par.extracted_data)


# Test the get_stored_data method
def test_get_stored_data(arxiv_par):
    # Call the store_data method with max_results = 5 and days = 60
    arxiv_par.store_data(max_results=5, days=60)

    # Call the get_stored_data method and store the result in a variable
    stored_data = arxiv_par.get_stored_data()

    # Check that the stored_data variable is a pandas dataframe with 5 rows and 7 columns
    assert isinstance(stored_data, pd.DataFrame)
    assert stored_data.shape == (5, 7)

    # Check that the stored_data variable contains the same data as the extracted_data attribute
    assert stored_data.equals(arxiv_par.extracted_data)
