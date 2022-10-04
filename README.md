# Arxiv Hunter

Using scripts from 'link to karpathys repo' for getting latest papers, downloading pdfs and converting pdfs to text
python -m venv venv
python -m venv venv
pip install -r requirements.txt

run fetch_papers
run download_pdfs
run parse_pdf_to_text
run process_text_file

Find relevant papers on arxiv.

Idea: Too many papers are posted on arxiv every day. It has become hard to find relevant papers and even harder to find papers with good ideas and important contributions. The main idea is to use machine learning to facilitate research and reduce its overhead.

Usage: Given your idea or what you want to see or read about(in a sentence or a para), this repo will try to find the most relevant texts spread across different papers and maybe come up with a idea tree.

Best possible end results:
1) It doesn't depend on classic metrics like number of citations, h-index of authors and exact keywords match.
2) It thinks in terms of ideas and concepts.
3) It gives me different ways of achieving the said idea or how things has been done till now.
4) Maybe it needs to learn from my behaviour. Which papers I found interesting, which were hoax. Something like off-policy learning.


#### Phases

##### Phase 1: 
Get contents of an online webpage. Perform summarization of the article no matter how big the article

    Phase 1.1: Deploy the result of above on a website : Currently here
    Phase 1.2: Article on SOA summarization

Resources:
python-goose for article extraction

##### Phase 2: Research paper summarization
Given a research paper link, summarize it and deploy it on the website.

    Phase 2.1: Build or find model for Research paper summarization.
    Phase 2.2: Check effectiveness of summarization with focus on novelty.
    Phase 2.3: Deploy

##### Phase 3: Multi-document summarization
Get contents of a Google search and try to summarize the results for the search

    Phase 3.1: SOA QA models
    Phase 3.2: QA on very large texts
    Phase 3.3: Deployment


