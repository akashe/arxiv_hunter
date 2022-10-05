import json
import os
import re
import tarfile
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

from data_utils import Config

import spacy
sentence_splitter = spacy.load("en_core_web_sm")

from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained(Config.tokenizer)


def clean_text(text):
    """
    Cleans the text by removing whitespaces
    """
    return re.sub(r'^\s+|\s+$|\s+'," ", text)


def get_abstract(text):
    """
    Return the abstract of a research paper
    :param text: the text body of the paper
    :return: abstract
    """
    abstract = ""
    possible_abstracts = \
    re.findall(r'Abstract\s+(.*)1\sIntroduction|ABSTRACT\s+(.*)1\sINTRODUCTION', text, flags=re.DOTALL)[0]
    for i__ in possible_abstracts:
        if i__ != "":
            abstract = i__

    return abstract


def generate_sentences(text):
    """
    Function to convert a blob of text or in this case the text extracted from
    a pdf into paragraphs of fixed maximum token length

    Code from: https://github.com/google-research/language/blob/6f34e9f35c836cb9ed438420f4e249440c656c00/language/orqa/preprocessing/wiki_preprocessor.py#L48
    """
    doc = sentence_splitter(text)
    sentences = [str(sentence) for sentence in doc.sents]

    current_token_count = 0
    current_block_sentences = []

    for sentence in sentences:
        num_tokens = len(tokenizer.tokenize(sentence))
        hypothetical_length = current_token_count + num_tokens

        if hypothetical_length <= Config.max_block_len:
            current_token_count += num_tokens
            current_block_sentences.append(sentence)

        else:
            yield " ".join(current_block_sentences).strip()
            current_token_count = num_tokens
            current_block_sentences = [sentence]

    if current_block_sentences:
        yield " ".join(current_block_sentences).strip()


def main():
    if not os.path.exists(Config.json_dir):
      print('creating ', Config.json_dir)
      os.makedirs(Config.json_dir)

    have = set(os.listdir(Config.json_dir))
    files = os.listdir(Config.txt_dir)

    for i,f in enumerate(files):
        json_basename = f[:-4] + '.json'

        if json_basename in have:
            print('%d/%d skipping %s, already exists.' % (i, len(files), json_basename))
            continue

        txt_path = os.path.join(Config.txt_dir, f)
        json_path = os.path.join(Config.json_dir, json_basename)

        # extract abstract and paragraphs from text file
        with open(txt_path,"r",encoding="utf=8") as txt_file:
            text = txt_file.read()

            # clean the text
            text = clean_text(text)

            # TODO: remove everything after references

            # get abstract of the paper
            abstract = get_abstract(text)

            if abstract == "":
                logger.error(f"Empty abstract for file {f}")
                continue

            # get paragraphs
            paras = list(generate_sentences(text))

        # save extracted information to json file
        with open(json_path,"w") as json_file:
            json_object = json.dumps({
                "file_name": f,
                "abstract": abstract,
                "paras": paras
            })

            json_file.write(json_object)

    # create a tar file for the jsons created
    jsons = set(os.listdir(Config.json_dir))
    with tarfile.open(os.path.join(Config.tar_dir,"processed.tar.gz"), "w:gz") as tar:
        for j in jsons:
            tar.add(os.path.join(Config.json_dir,j))


if __name__ == "__main__":
    main()

