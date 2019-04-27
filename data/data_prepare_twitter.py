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
final = '/media/hector/DATA/datalab-data/twitter_j2018_full.csv'

# use glob to read all the files from the path
files = glob.glob(path)

## read a sample file
f = open('/media/hector/DATA/datalab-data/combined_file/keys/100/10029320.txt').readlines()

## check the keys in the dict
d_1 = json.loads(f[29])
d_2 = json.loads(f[37])
d_3 = json.loads(f[39])
d_4 = json.loads(f[49])
d_5 = json.loads(f[41])
d_6 = json.loads(f[20])


## print the keys for 'posts'
print("Keys in the dict 'posts'", d_1['posts'].keys())

## print the keys for twitter
print("Keys in the dict 'posts{twitter}'", d_1['posts']['twitter'][0].keys())

## print the keys for facebook
print("Keys in the dict 'posts{facebook}'", d_1['posts']['facebook'][0].keys())

## print the keys for blogs
print("Keys in the dict 'posts{blogs}'", d_2['posts']['blogs'][0].keys())

## print the keys for policy
print("Keys in the dict 'posts{policy}'", d_3['posts']['policy'][0].keys())

## print the keys for patent
print("Keys in the dict 'posts{patent}'", d_4['posts']['patent'][0].keys())

## print the keys for googleplus
print("Keys in the dict 'posts{googleplus}'", d_5['posts']['googleplus'][0].keys())

## print the keys for wikipedia
print("Keys in the dict 'posts{wikipedia}'", d_6['posts']['wikipedia'][0].keys())

# write the file to a csv
'''
{'rt': ['FrontImmunol'],
 'license': 'gnip',
 'author': {'name': 'Monica',
  'url': 'http://linkedin.com/in/monicascdreis',
  'image': 'https://pbs.twimg.com/profile_images/946314369578696704/2TXhbQTE_normal.jpg',
  'tweeter_id': '1887350696',
  'followers': 607,
  'id_on_source': 'Sophitia_Rin',
  'geo': {'ln': -71.05977, 'country': 'US', 'lt': 42.35843},
  'description': 'Stem cell and EV/Exosome scientist! An european exploring the world! @harvardmed #Immunology #scifigeek #musiclover #worldcitizen'},
 'url': 'http://twitter.com/Sophitia_Rin/statuses/905451053340135424',
 'citation_ids': [24173673],
 'tweet_id': '905451053340135424',
 'posted_on': '2017-09-06T15:22:08+00:00'}
'''
with open(final, 'w') as final_file:
    datawriter = csv.writer(final_file, delimiter=',',quotechar='|',
                            quoting=csv.QUOTE_MINIMAL)
    datawriter.writerow(['altmetric_id', 'tweet_id', 'tweet_url',
                         'tweet_post_date', 'twitter_author_url',
                         'twitter_author_description', 'twitter_author_id',
                         'twitter_author_handle', 'twitter_author_followers',
                         'twitter_author_name', 'paper_title', 'paper_abstract',
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
                        if 'posts' in data and 'twitter' in data['posts']:
                            for post in data['posts']['twitter']:
                                tweet_id = []
                                tweet_url = []
                                tweet_post_date = []
                                twitter_author_url = []
                                twitter_author_description = []
                                twitter_author_id = []
                                twitter_author_handle = []
                                twitter_author_followers = []
                                twitter_author_name = []
                                if 'tweet_id' in post:
                                    tweet_id.append(str(post['tweet_id']))
                                else:
                                    tweet_id = np.nan
                                if 'url' in post:
                                    tweet_url.append(str(post['url']))
                                else:
                                    tweet_url = np.nan
                                if 'posted_on' in post:
                                    tweet_post_date.append(str(post['posted_on']))
                                else:
                                    tweet_post_date = np.nan
                                if 'author' in post and 'url' in post['author']:
                                    twitter_author_url.append(str(post['author']['url']))
                                else:
                                    twitter_author_url = np.nan
                                if 'author' in post and 'description' in post['author']:
                                    twitter_author_description.append(str(post['author']['description']))
                                else:
                                    twitter_author_description = np.nan
                                if 'author' in post and 'tweeter_id' in post['author']:
                                    twitter_author_id.append(post['author']['tweeter_id'])
                                else:
                                    twitter_author_id = np.nan
                                #
                                if 'author' in post and 'id_on_source' in post['author']:
                                    twitter_author_handle.append(post['author']['id_on_source'])
                                else:
                                    twitter_author_handle = np.nan
                                if 'author' in post and 'followers' in post['author']:
                                    twitter_author_followers.append(post['author']['followers'])
                                else:
                                    twitter_author_followers = np.nan
                                if 'author' in post and 'name' in post['author']:
                                    twitter_author_name.append(post['author']['name'])
                                else:
                                    twitter_author_name = np.nan
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
                            datawriter.writerow([altmetric_id, tweet_id, tweet_url,
                         tweet_post_date, twitter_author_url,
                         twitter_author_description, twitter_author_id,
                         twitter_author_handle, twitter_author_followers,
                         twitter_author_name, paper_title, paper_abstract,
                         paper_doi, paper_pubdate, paper_subjects,
                         paper_publisher_subjects, paper_scopus_subjects])
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise
