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
final = '/media/hector/DATA/datalab-data/facebook_j2018_full.csv'

# use glob to read all the files from the path
files = glob.glob(path)

## read a sample file
f = open('/media/hector/DATA/datalab-data/combined_file/keys/100/10029320.txt').readlines()

## check the keys in the dict
d_1 = json.loads(f[29])

## print the keys for facebook
print("Keys in the dict 'posts{facebook}'", d_1['posts']['facebook'][0].keys())

# write the file to a csv
'''
{
  'license': 'public',
  'title': 'Transfer of Methylprednisolone into Breast Milk in a Mother with Multiple Sclerosis',
  'url': 'https://www.facebook.com/permalink.php?story_fbid=1027446043938962&id=508976565785915',
  'author': {'url': 'https://www.facebook.com/508976565785915',
   'facebook_wall_name': 'Journal of Human Lactation',
   'image': 'https://graph.facebook.com/508976565785915/picture',
   'id_on_source': '508976565785915',
   'name': 'Journal of Human Lactation'},
  'summary': 'New Papers OnlineFirst at JHL!\n\nCase Report\n\nTransfer of Methylprednisolone into Breast Milk in a Mother with Multiple Sclerosis\n\nBy Cooper et al.\nhttp://jhl.sagepub.com/content/early/2015/02/12/0890334415570970.full\n\n\nInsights in Policy\n\nHow Research on C',
  'citation_ids': [3713571, 3713588],
  'posted_on': '2015-02-18T23:00:01+00:00'
}
'''
with open(final, 'w') as final_file:
    datawriter = csv.writer(final_file, delimiter=',',quotechar='|',
                            quoting=csv.QUOTE_MINIMAL)
    datawriter.writerow(['altmetric_id', 'fb_post_title', 'fb_post_url',
                         'fb_post_description', 'fb_post_date',
                         'fb_author_url', 'fb_author_name', 'paper_title',
                         'paper_abstract', 'paper_doi', 'paper_pubdate',
                         'paper_subjects', 'paper_publisher_subjects',
                         'paper_scopus_subjects'])

    # the exception handling block
    for file in tqdm(files):
        try:
            with open(file) as f:
                for text_data in f.readlines():
                    data = json.loads(text_data)
                    if 'altmetric_id' in data:
                        altmetric_id = data['altmetric_id']
                        if 'posts' in data and 'facebook' in data['posts']:
                            for post in data['posts']['facebook']:
                                fb_post_title = []
                                fb_post_url = []
                                fb_post_description = []
                                fb_post_date = []
                                fb_author_url = []
                                fb_author_name = []
                                if 'title' in post:
                                    fb_post_title.append(str(post['title']))
                                else:
                                    fb_post_title = np.nan
                                if 'url' in post:
                                    fb_post_url.append(str(post['url']))
                                else:
                                    fb_post_url = np.nan
                                if 'summary' in post:
                                    fb_post_description.append(str(post['summary']))
                                else:
                                    fb_post_description = np.nan
                                if 'posted_on' in post:
                                    fb_post_date.append(str(post['posted_on']))
                                else:
                                    fb_post_date = np.nan
                                if 'author' in post and 'url' in post['author']:
                                    fb_author_url.append(str(post['author']['url']))
                                else:
                                    fb_author_url = np.nan
                                if 'author' in post and 'name' in post['author']:
                                    fb_author_name.append(post['author']['name'])
                                else:
                                    fb_author_name = np.nan
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
                            datawriter.writerow([altmetric_id, fb_post_title, fb_post_url,
                         fb_post_description, fb_post_date, fb_author_url,
                         fb_author_name, paper_title, paper_abstract,
                         paper_doi, paper_pubdate, paper_subjects,
                         paper_publisher_subjects, paper_scopus_subjects])
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise
