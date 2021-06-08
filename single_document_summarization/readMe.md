# Single Document summarization

This folder contains scripts to scrap, summarize and deploy for single document summarization. We will use a longformer to summarize very long articles and BART for smaller texts. We will deploy the models using torchserve on a domain yet to be chosen.

We will be using python-goose to extract text from articles.

#### Usage:

Setup virtual environment
```
cd single_document_summarization
python3 -m venv summarization_venv
source summarization_venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt --use-feature=2020-resolver
```

Set up python-goose for article extraction
```
git clone https://github.com/akashe/python-goose.git
pip install -r python-goose/requirements.txt
python python-goose/setup.py install
rm -rf python-goose/.git
rm -rf python-goose/
```

