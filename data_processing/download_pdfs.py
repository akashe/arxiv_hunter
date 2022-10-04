import os
import time
import pickle
import shutil
import random
from  urllib.request import urlopen
import multiprocessing

from data_utils import Config

#####
# Copied and modified from https://github.com/karpathy/arxiv-sanity-preserver/blob/master/download_pdfs.py
#####

 # after this many seconds we give up on a paper
if not os.path.exists(Config.pdf_dir): os.makedirs(Config.pdf_dir)
have = set(os.listdir(Config.pdf_dir)) # get list of all pdfs we already have

db = pickle.load(open(Config.db_path, 'rb'))

def download_files(db):
  timeout_secs = 10
  numok = 0
  numtot = 0

  for pid, j in db.items():

    pdfs = [x['href'] for x in j['links'] if x['type'] == 'application/pdf']
    assert len(pdfs) == 1
    pdf_url = pdfs[0] + '.pdf'
    basename = pdf_url.split('/')[-1]
    fname = os.path.join(Config.pdf_dir, basename)

    # try retrieve the pdf
    numtot += 1
    try:
      if not basename in have:
        print('fetching %s into %s' % (pdf_url, fname))
        req = urlopen(pdf_url, None, timeout_secs)
        with open(fname, 'wb') as fp:
          shutil.copyfileobj(req, fp)
        # time.sleep(0.05 + random.uniform(0,0.1))
        time.sleep(0.02)
      else:
        print('%s exists, skipping' % (fname,))
      numok += 1
    except Exception as e:
      print('error downloading: ', pdf_url)
      print(e)

    print('%d/%d of %d downloaded ok.' % (numok, numtot, len(db)))


num_threads = 6
split_dicts = []
for i in range(num_threads):
  split_dicts.append(dict(list(db.items())[i*len(db)//num_threads:(i+1)*len(db)//num_threads]))

process_list = []
for i in split_dicts:
  p = multiprocessing.Process(target=download_files, args=[i])
  p.start()
  process_list.append(p)

for process in process_list:
  process.join()
  
#print('final number of papers downloaded okay: %d/%d' % (numok, len(db)))

