# This Source Code Form is subject to the terms of the MPL
# License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/akhilpandey95/altpred/blob/master/LICENSE.

import os
import csv
import sys
import glob
import json
import errno
import random
import string
import spacy as sp
import numpy as np
import pandas as pd
import seaborn as sns
from tqdm import tqdm
import tensorflow as tf
import matplotlib.pyplot as plt
from collections import defaultdict
from matplotlib.pyplot import figure
from sklearn.preprocessing import MinMaxScaler

# read the complete dataset
data = pd.read_csv("../pubundsci/combined_dataset_charlie.csv", index_col=0)


# take 1% fraction
data = data.sample(frac=0.01).reset_index(drop=True)

# reset the index once again
data = data.sample(frac=1).reset_index(drop=True)

# print the head of the dataset
data.head()

# data.to_csv("sampled_dataset_alpha.csv", sep = ',', encoding="utf-8")
data = pd.read_csv("sampled_dataset_charlie.csv", index_col=0)

# Scatter plots of the altmetric scores observed for articles with age of 1 day, 3 day and 4 days
# set the sns style as ticks
sns.set(style='ticks')

# create the figure and axes for the subplot
f, axes = plt.subplots(1, 3, figsize=(18,8))

# load the scatterplot matrix for the 1 day target variable
sns.scatterplot(y='altmetric_score_1d', x=list(range(len(data))) ,data=data, ax=axes[0])

# load the scatter plot matrix for the 3 day target variable
sns.scatterplot(y='altmetric_score_3d', x=list(range(len(data))) ,data=data, ax=axes[1])

# load the scatter plot matrix for the 4 day target variable
sns.scatterplot(y='altmetric_score_4d', x=list(range(len(data))) ,data=data, ax=axes[2])


# Scatter plots of the altmetric scores observed for articles with age of 6 days, 1 week and 1 month

# set the sns style as ticks
sns.set(style='ticks')

# create the figure and axes for the subplot
f, axes = plt.subplots(1, 3, figsize=(18,8))

# load the scatterplot matrix for the 6 days target variable
sns.scatterplot(y='altmetric_score_6d', x=list(range(len(data))) ,data=data, ax=axes[0])

# load the scatter plot matrix for the 1 week target variable
sns.scatterplot(y='altmetric_score_1w', x=list(range(len(data))) ,data=data, ax=axes[1])

# load the scatter plot matrix for the 1 month target variable
sns.scatterplot(y='altmetric_score_1m', x=list(range(len(data))) ,data=data, ax=axes[2])


# Scatter plots of the altmetric scores observed for articles with age of 3 months, 6 months and 1 year
# set the sns style as ticks
sns.set(style='ticks')

# create the figure and axes for the subplot
f, axes = plt.subplots(1, 3, figsize=(18,8))

# load the scatterplot matrix for the 3 month target variable
sns.scatterplot(y='altmetric_score_3m', x=list(range(len(data))) ,data=data, ax=axes[0])

# load the scatter plot matrix for the 6 months target variable
sns.scatterplot(y='altmetric_score_6m', x=list(range(len(data))) ,data=data, ax=axes[1])

# load the scatter plot matrix for the 1 year target variable
sns.scatterplot(y='altmetric_score_1y', x=list(range(len(data))) ,data=data, ax=axes[2])


#  Boxplots of all the target variables
figure(num=None, figsize=(16, 8), dpi=80, facecolor='w', edgecolor='k')

# create a boxplot for all the features
sns.boxplot(data=data.iloc[:, [
    data.columns.get_loc('altmetric_score_3d'),
    data.columns.get_loc('altmetric_score_1w'),
    data.columns.get_loc('altmetric_score_1m'),
    data.columns.get_loc('altmetric_score_3m'),
    data.columns.get_loc('altmetric_score_6m'),
    data.columns.get_loc('altmetric_score_1y')]])

data.columns

# read the directory
path = '/media/hector/DATA/datalab-data/combined_file/keys/*/*.txt'
final = '/media/hector/DATA/datalab-data/altmetrics_j2018_full.csv'

# use glob to read all the files from the path
files = glob.glob(path)

with open(final, 'w') as final_file:
    datawriter = csv.writer(final_file, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    datawriter.writerow(['altmetric_id','mendeley_readers','citeulikereaders','connoteareaders',
        'blog_users','blogs_posts_count','news_unique_users','total_posts_count',
        'wiki_posts_count','facebook_users','facebook_posts','twitter_users',
        'twitter_posts','citation_page','other_articles','mean','rank','perc',
        'scored_higher_than','sample_size','users_lecturer','users_librarian',
        'users_student_bachelor','users_student_master','users_student_pg',
        'users_student_phd','users_student_doct','users_researcher','users_other',
        'users_prof_assoc','users_prof','users_medi','users_ss','users_psych',
        'users_earth','users_agri','users_arts','users_us','users_th','users_ie',
        'users_id','users_au','users_gb','altmetric_score','altmetric_score_1y',
        'altmetric_score_6m','altmetric_score_3m','altmetric_score_1m',
        'altmetric_score_1w','altmetric_score_6d','altmetric_score_5d',
        'altmetric_score_4d','altmetric_score_3d','altmetric_score_3d',
        'altmetric_score_1d'])

    for file in tqdm(files):
        try:
            with open(file) as f:
                for text_data in f.readlines():
                    count = 0
                    data = json.loads(text_data)
                    if 'altmetric_id' in data:
                        altmetric_id=data['altmetric_id']
                        if 'counts' in data and 'readers' in data['counts'] and 'mendeley' in data['counts']['readers'] and isinstance(data['counts']['readers']['mendeley'], int):
                            mendeley_readers=data['counts']['readers']['mendeley']
                            count+=1
                        else:
                            mendeley_readers=0
                        if 'counts' in data and 'readers' in data['counts'] and 'citeulike' in data['counts']['readers'] and isinstance(data['counts']['readers']['citeulike'], int):
                            citeulikereaders=data['counts']['readers']['citeulike']
                            count+=1
                        else:
                            citeulikereaders=0
                        if 'counts' in data and 'readers' in data['counts'] and 'connotea' in data['counts']['readers'] and isinstance(data['counts']['readers']['connotea'], int):
                            connoteareaders=data['counts']['readers']['connotea']
                            count+=1
                        else:
                            connoteareaders=0
                        if 'counts' in data and 'blogs' in data['counts'] and 'unique_users_count' in data['counts']['blogs'] and isinstance(data['counts']['blogs']['unique_users_count'], int):
                            blog_users=data['counts']['blogs']['unique_users_count']
                            count+=1
                        else:
                            blog_users=0
                        if 'counts' in data and 'blogs' in data['counts'] and 'posts_count' in data['counts']['blogs'] and isinstance(data['counts']['blogs']['posts_count'], int):
                            blogs_posts_count=data['counts']['blogs']['posts_count']
                            count+=1
                        else:
                            blogs_posts_count=0
                        if 'counts' in data and 'news' in data['counts'] and isinstance(data['counts']['news']['unique_users_count'], int):
                            news_unique_users=data['counts']['news']['unique_users_count']
                            count+=1
                        else:
                            news_unique_users=0
                        if 'counts' in data and 'total' in data['counts'] and 'posts_count' in data['counts']['total'] and isinstance(data['counts']['total']['posts_count'], int):
                            total_posts_count=data['counts']['total']['posts_count']
                            count+=1
                        else:
                            total_posts_count=0
                        if 'counts' in data and 'wikipedia' in data['counts'] and isinstance(data['counts']['wikipedia']['unique_users_count'], int):
                            wiki_posts_count=data['counts']['wikipedia']['unique_users_count']
                            count+=1
                        else:
                            wiki_posts_count=0
                        if 'startpage' in data['citation'] and isinstance(data['citation']['startpage'], int):
                            citation_page=data['citation']['startpage']
                            count+=1
                        else:
                            citation_page=0
                        if 'counts' in data and 'facebook' in data['counts'] and 'unique_users_count' in data['counts']['facebook']:
                            facebook_users=data['counts']['facebook']['unique_users_count']
                            count+=1
                        else:
                            facebook_users=0
                        if 'counts' in data and 'facebook' in data['counts'] and 'posts_count' in data['counts']['facebook']:
                            facebook_posts=data['counts']['facebook']['posts_count']
                            count+=1
                        else:
                            facebook_posts=0
                        if 'counts' in data and 'twitter' in data['counts'] and 'unique_users_count' in data['counts']['twitter']:
                            twitter_users=data['counts']['twitter']['unique_users_count']
                            count+=1
                        else:
                            twitter_users=0
                        if 'counts' in data and 'twitter' in data['counts'] and 'posts_count' in data['counts']['twitter']:
                            twitter_posts=data['counts']['twitter']['posts_count']
                            count+=1
                        else:
                            twitter_posts=0
                        altmetric_score = data['altmetric_score']['score']
                        if data['altmetric_score']['score_history'] != None and '1y' in data['altmetric_score']['score_history'] and isinstance(data['altmetric_score']['score_history']['1y'], int):
                            altmetric_score_1y=data['altmetric_score']['score_history']['1y']
                            count+=1
                        else:
                            altmetric_score_1y=0
                        if data['altmetric_score']['score_history'] != None and '6m' in data['altmetric_score']['score_history'] and isinstance(data['altmetric_score']['score_history']['6m'], int):
                            altmetric_score_6m=data['altmetric_score']['score_history']['6m']
                            count+=1
                        else:
                            altmetric_score_6m=0
                        if data['altmetric_score']['score_history'] != None and '3m' in data['altmetric_score']['score_history'] and isinstance(data['altmetric_score']['score_history']['3m'], int):
                            altmetric_score_3m=data['altmetric_score']['score_history']['3m']
                            count+=1
                        else:
                            altmetric_score_3m=0
                        if data['altmetric_score']['score_history'] != None and '1m' in data['altmetric_score']['score_history'] and isinstance(data['altmetric_score']['score_history']['1m'], int):
                            altmetric_score_1m=data['altmetric_score']['score_history']['1m']
                            count+=1
                        else:
                            altmetric_score_1m=0
                        if data['altmetric_score']['score_history'] != None and '1w' in data['altmetric_score']['score_history'] and isinstance(data['altmetric_score']['score_history']['1w'], int):
                            altmetric_score_1w=data['altmetric_score']['score_history']['1w']
                            count+=1
                        else:
                            altmetric_score_1w=0
                        if data['altmetric_score']['score_history'] != None and '6d' in data['altmetric_score']['score_history'] and isinstance(data['altmetric_score']['score_history']['6d'], int):
                            altmetric_score_6d=data['altmetric_score']['score_history']['6d']
                            count+=1
                        else:
                            altmetric_score_6d=0
                        if data['altmetric_score']['score_history'] != None and '5d' in data['altmetric_score']['score_history'] and isinstance(data['altmetric_score']['score_history']['5d'], int):
                            altmetric_score_5d=data['altmetric_score']['score_history']['5d']
                            count+=1
                        else:
                            altmetric_score_5d=0
                        if data['altmetric_score']['score_history'] != None and '4d' in data['altmetric_score']['score_history'] and isinstance(data['altmetric_score']['score_history']['4d'], int):
                            altmetric_score_4d=data['altmetric_score']['score_history']['4d']
                            count+=1
                        else:
                            altmetric_score_4d=0
                        if data['altmetric_score']['score_history'] != None and '3d' in data['altmetric_score']['score_history'] and isinstance(data['altmetric_score']['score_history']['3d'], int):
                            altmetric_score_3d=data['altmetric_score']['score_history']['3d']
                            count+=1
                        else:
                            altmetric_score_3d=0
                        if data['altmetric_score']['score_history'] != None and '1d' in data['altmetric_score']['score_history'] and isinstance(data['altmetric_score']['score_history']['1d'], int):
                            altmetric_score_1d=data['altmetric_score']['score_history']['1d']
                            count+=1
                        else:
                            altmetric_score_1d=0
                        if data['altmetric_score']['context_for_score'] != None and 'total_number_of_other_articles' in data['altmetric_score']['context_for_score']['all'] and isinstance(data['altmetric_score']['context_for_score']['all']['total_number_of_other_articles'], int):
                            other_articles=data['altmetric_score']['context_for_score']['all']['total_number_of_other_articles']
                            count+=1
                        else:
                            other_articles=0
                        if data['altmetric_score']['context_for_score']!=None and 'mean' in data['altmetric_score']['context_for_score']['all']:
                            mean=data['altmetric_score']['context_for_score']['all']['mean']
                            count+=1
                        else:
                            mean=0
                        if data['altmetric_score']['context_for_score']!=None and 'rank' in data['altmetric_score']['context_for_score']['all']:
                            rank=data['altmetric_score']['context_for_score']['all']['rank']
                            count+=1
                        else:
                            rank=0
                        if data['altmetric_score']['context_for_score']!=None and 'this_scored_higher_than_pct' in data['altmetric_score']['context_for_score']['all']:
                            perc=data['altmetric_score']['context_for_score']['all']['this_scored_higher_than_pct']
                            count+=1
                        else:
                            perc=0
                        if data['altmetric_score']['context_for_score']!=None and 'this_scored_higher_than' in data['altmetric_score']['context_for_score']['all']:
                            scored_higher_than=data['altmetric_score']['context_for_score']['all']['this_scored_higher_than']
                            count+=1
                        else:
                            scored_higher_than=0
                        if data['altmetric_score']['context_for_score']!=None and 'sample_size' in data['altmetric_score']['context_for_score']['all']:
                            sample_size=data['altmetric_score']['context_for_score']['all']['sample_size']
                            count+=1
                        else:
                            sample_size=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Librarian' in data['demographics']['users']['mendeley']['by_status']:
                            users_librarian=data['demographics']['users']['mendeley']['by_status']['Librarian']
                            count+=1
                        else:
                            users_librarian=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Lecturer' in data['demographics']['users']['mendeley']['by_status']:
                            users_lecturer=data['demographics']['users']['mendeley']['by_status']['Lecturer']
                            count+=1
                        else:
                            users_lecturer=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Student > Bachelor' in data['demographics']['users']['mendeley']['by_status']:
                            users_student_bachelor=data['demographics']['users']['mendeley']['by_status']['Student  > Bachelor']
                            count+=1
                        else:
                            users_student_bachelor=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Student > Master' in data['demographics']['users']['mendeley']['by_status']:
                            users_student_master=data['demographics']['users']['mendeley']['by_status']['Student  > Master']
                            count+=1
                        else:
                            users_student_master=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Student > Postgraduate' in data['demographics']['users']['mendeley']['by_status']:
                            users_student_pg=data['demographics']['users']['mendeley']['by_status']['Student  > Postgraduate']
                            count+=1
                        else:
                            users_student_pg=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Student  > Ph. D. Student' in data['demographics']['users']['mendeley']['by_status']:
                            users_student_phd=data['demographics']['users']['mendeley']['by_status']['Student  > Ph. D. Student']
                            count+=1
                        else:
                            users_student_phd=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Student  > Doctoral Student' in data['demographics']['users']['mendeley']['by_status']:
                            users_student_doct=data['demographics']['users']['mendeley']['by_status']['Student  > Doctoral Student']
                            count+=1
                        else:
                            users_student_doct=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Researcher' in data['demographics']['users']['mendeley']['by_status']:
                            users_researcher=data['demographics']['users']['mendeley']['by_status']['Researcher']
                            count+=1
                        else:
                            users_researcher=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Other' in data['demographics']['users']['mendeley']['by_status']:
                            users_other=data['demographics']['users']['mendeley']['by_status']['Other']
                            count+=1
                        else:
                            users_other=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Professor > Associate Professor' in data['demographics']['users']['mendeley']['by_status']:
                            users_prof_assoc=data['demographics']['users']['mendeley']['by_status']['Professor > Associate Professor']
                            count+=1
                        else:
                            users_prof_assoc=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Professor' in data['demographics']['users']['mendeley']['by_status']:
                            users_prof=data['demographics']['users']['mendeley']['by_status']['Professor']
                            count+=1
                        else:
                            users_prof=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Medicine and Dentistry' in data['demographics']['users']['mendeley']['by_discipline']:
                            users_medi=data['demographics']['users']['mendeley']['by_discipline']['Medicine and Dentistry']
                            count+=1
                        else:
                            users_medi=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Social Sciences' in data['demographics']['users']['mendeley']['by_discipline']:
                            users_ss=data['demographics']['users']['mendeley']['by_discipline']['Social Sciences']
                            count+=1
                        else:
                            users_ss=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Psychology' in data['demographics']['users']['mendeley']['by_discipline']:
                            users_psych=data['demographics']['users']['mendeley']['by_discipline']['Psychology']
                            count+=1
                        else:
                            users_psych=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Earth and Planetary Sciences' in data['demographics']['users']['mendeley']['by_discipline']:
                            users_earth=data['demographics']['users']['mendeley']['by_discipline']['Earth and Planetary Sciences']
                            count+=1
                        else:
                            users_earth=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Agricultural and Biological Sciences' in data['demographics']['users']['mendeley']['by_discipline']:
                            users_agri=data['demographics']['users']['mendeley']['by_discipline']['Agricultural and Biological Sciences']
                            count+=1
                        else:
                            users_agri=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Arts and Humanities' in data['demographics']['users']['mendeley']['by_discipline']:
                            users_arts=data['demographics']['users']['mendeley']['by_discipline']['Arts and Humanities']
                            count+=1
                        else:
                            users_arts=0
                        if 'geo' in data['demographics'] and 'mendeley' in data['demographics']['geo']:
                            if 'US' in data['demographics']['geo']['mendeley']:
                                users_us=data['demographics']['geo']['mendeley']['US']
                                count+=1
                            else:
                                users_us=0
                            if 'TH' in data['demographics']['geo']['mendeley']:
                                users_th=data['demographics']['geo']['mendeley']['TH']
                                count+=1
                            else:
                                users_th=0
                            if 'IE' in data['demographics']['geo']['mendeley']:
                                users_ie=data['demographics']['geo']['mendeley']['IE']
                                count+=1
                            else:
                                users_ie=0
                            if 'ID' in data['demographics']['geo']['mendeley']:
                                users_id=data['demographics']['geo']['mendeley']['ID']
                                count+=1
                            else:
                                users_id=0
                            if 'AU' in data['demographics']['geo']['mendeley']:
                                users_au=data['demographics']['geo']['mendeley']['AU']
                                count+=1
                            else:
                                users_au=0
                            if 'GB' in data['demographics']['geo']['mendeley']:
                                users_gb=data['demographics']['geo']['mendeley']['GB']
                                count+=1
                            else:
                                users_gb=0
                        else:
                            users_us=0
                            users_th=0
                            users_ie=0
                            users_id=0
                            users_au=0
                            users_gb=0
                        if count>30:
                            datawriter.writerow([altmetric_id,mendeley_readers,citeulikereaders,connoteareaders,blog_users,blogs_posts_count,news_unique_users,total_posts_count,wiki_posts_count,facebook_users,facebook_posts,twitter_users,twitter_posts,citation_page,other_articles,mean,rank,perc,scored_higher_than,sample_size,users_lecturer,users_student_bachelor,users_student_master,users_student_pg,users_student_phd,users_student_doct,users_researcher,users_other,users_prof_assoc,users_prof,users_medi,users_ss,users_psych,users_earth,users_agri,users_arts,users_us,users_th,users_ie,users_id,users_au,users_gb,altmetric_score,altmetric_score_1y,altmetric_score_6m,altmetric_score_3m,altmetric_score_1m,altmetric_score_1w,altmetric_score_6d,altmetric_score_5d,altmetric_score_4d,altmetric_score_3d,altmetric_score_3d,altmetric_score_1d])
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise
