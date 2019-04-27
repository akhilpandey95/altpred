# This Source Code Form is subject to the terms of the MPL
# License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/akhilpandey95/altpred/blob/master/LICENSE.

import csv
import glob
import json
import numpy as np
from tqdm import tqdm
import dask.dataframe as dd

# read the directory
path = '/media/hector/DATA/datalab-data/combined_file/keys/*/*.txt'
final = '/media/hector/DATA/datalab-data/blogs_j2018_full.csv'

# use glob to read all the files from the path
files = glob.glob(path)

## read a sample file
f = open('/media/hector/DATA/datalab-data/combined_file/keys/100/10000556.txt').readlines()

## check the keys in the dict
d_1 = json.loads(f[19])

## print the keys for blogs
print("Keys in the dict 'posts{blogs}'", d_1['posts']['blogs'][0].keys())

# write the file to a csv
'''
{'title': 'Vitamin D deficiency and Chronic Fatigue Syndrome',
 'url': 'http://questioning-answers.blogspot.com/2012/10/vitamin-d-deficiency-and-chronic-fatigue-syndrome.html',
 'license': 'public',
 'citation_ids': [1200711,
  1485287,
  253880,
  1485289,
  1485290,blogs_j2018_full
  1485291,
  1485292],
 'posted_on': '2012-10-08T14:02:00+00:00',
 'summary': 'Vitamin D3 @ Wikipedia\xa0I have no hesitation in admitting to being more than a little bit "obsessive" about my data capture and the volumes of lovely, yummy science-y research alerts it produces. Indeed quite a bit of said research ends up as fodder for thi',
 'author': {'name': 'Questioning Answers',
  'url': 'http://questioning-answers.blogspot.com/',
  'description': 'Views on autism research and other musings.'}}
'''
with open(final, 'w') as final_file:
    datawriter = csv.writer(final_file, delimiter=',',quotechar='|',
                            quoting=csv.QUOTE_MINIMAL)
    datawriter.writerow(['altmetric_id', 'blog_title', 'blog_url',
                         'blog_summary', 'blog_pub_on', 'blog_author_name'
                         'blog_author_url', 'paper_title', 'paper_abstract',
                         'paper_doi', 'paper_pubdate', 'paper_subjects',
                         'paper_publisher_subjects', 'paper_scopus_subjects'])

    # the exception handling block
    for file in tqdm(files):
        try:
            with open(file) as f:
                for text_data in f.readlines():
                    data = json.loads(text_data)
                    if 'altmetric_id' in data:
                        altmetric_id = data['altmetric_id']
                        if 'posts' in data and 'blogs' in data['posts']:
                            for post in data['posts']['blogs']:
                                blog_title = []
                                blog_url = []
                                blog_summary = []
                                blog_pub_on = []
                                blog_author_name = []
                                blog_author_url = []
                                if 'title' in post:
                                    blog_title.append(str(post['title']))
                                else:
                                    blog_title = np.nan
                                if 'url' in post:
                                    blog_url.append(str(post['url']))
                                else:
                                    blog_url = np.nan
                                if 'summary' in post:
                                    blog_summary.append(str(post['summary']))
                                else:
                                    blog_summary = np.nan
                                if 'posted_on' in post:
                                    blog_pub_on.append(str(post['posted_on']))
                                else:
                                    blog_pub_on = np.nan
                                if 'author' in post and 'name' in post['author']:
                                    blog_author_name.append(post['author']['name'])
                                else:
                                    blog_author_name = np.nan
                                if 'author' in post and 'url' in post['author']:
                                    blog_author_url.append(str(post['author']['url']))
                                else:
                                    blog_author_url = np.nan
                            if 'title' in data['citation']:
                                paper_title = str(data['citation']['title'])
                            else:
                                paper_title = np.nan
                            if 'abstract' in data['citation']:
                                paper_abstract = str(data['citation']['abstract'])
                            else:
                                paper_abstract = np.nan
                            if 'doi' in data['citation']:
                                paper_doi = str(data['citation']['doi'])
                            else:
                                paper_doi = np.nan
                            if 'pubdate' in data['citation']:
                                paper_pubdate = str(data['citation']['pubdate'])
                            else:
                                paper_pubdate = np.nan
                            if 'subjects' in data['citation']:
                                paper_subjects = str(data['citation']['subjects'])
                            else:
                                paper_subjects = np.nan
                            if 'publisher_subjects' in data['citation']:
                                paper_publisher_subjects = str(data['citation']['publisher_subjects'])
                            else:
                                paper_publisher_subjects = np.nan
                            if 'scopus_subjects' in data['citation']:
                                paper_scopus_subjects = str(data['citation']['scopus_subjects'])
                            else:
                                paper_scopus_subjects = np.nan
                            datawriter.writerow([altmetric_id, blog_title, blog_url, blog_summary, blog_pub_on, blog_author_name, blog_author_url, paper_title, paper_abstract, paper_doi, paper_pubdate,paper_subjects, paper_publisher_subjects, paper_scopus_subjects])
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise
