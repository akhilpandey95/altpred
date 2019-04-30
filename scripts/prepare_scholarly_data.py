# This Source Code Form is subject to the terms of the MPL
# License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/akhilpandey95/altpred/blob/master/LICENSE.

import sys
import pandas as pd
from tqdm import tqdm
from datetime import datetime
from altmetric_api import add_all_info, add_pubdate

# function for preparing the 2014 altmetrics dataset
def data_load(file_path):
    """
    Clean and prepare the 2014 altmetrics dataset

    Parameters
    ----------
    No arguments

    Returns
    -------
    Dataframe
        pandas.DataFrame

    """

    try:
        # read the dataset first
        data = pd.read_csv(file_path, sep='\t')

        # remove all the unecessary columns
        data = data.drop(columns=['DOI', 'SCORE', 'PMID', 'ARXIV_ID', 'HANDLE', 'FACEBOOK_WALLS', 'BLOGS', 'GPLUS_ACCOUNTS', 'NEWS_OUTLETS'])

        # return the dataframe
        return data
    except:
        return pd.DataFrame()

# function for returning year from an epoch
def get_year_from_epoch(epoch):
    """
    Obtain the year from a given epoch string

    Parameters
    ----------
    arg1 | epoch: str
        Epoch string

    Returns
    -------
    Number
        int

    """
    return datetime.datetime.fromtimestamp(epoch).year

# function for eliminating unecessary rows
def eliminate_row_by_pubdate(data_frame):
    """
    Process the dataset and collect all the meta infromation for the 2014 altmetrics dataset

    Parameters
    ----------
    arg1 | data_frame: pandas.DataFrame
        A loaded dataframe with just ID, twitter count

    Returns
    -------
    Dataframe
        pandas.DataFrame

    """
    try:
        # first collect the pubdate of every article
        data_frame = data_frame.assign(pub_date = [add_pubdate(x) for x in tqdm(data_frame['ID'])])

        # drop the row whose row value is an empty string
        data_frame = data_frame[data_frame.pub_date != '']

        # remove the rows whose year of publishing is prior to 2014
        data_frame = data_frame[date_frame['pub_date'].apply(get_year_from_epoch) == 2014]

        # reset the dataframe index
        data_frame = data_frame.reset_index(drop=True)
        
        # return the modified dataframe
        return data_frame
    except:
        # return the original dataframe
        return data_frame
    
# function for processing the dataset
def data_processing(data_frame):
    """
    Process the dataset and collect all the meta infromation for the 2014 altmetrics dataset

    Parameters
    ----------
    arg1 | data_frame: pandas.DataFrame
        A loaded dataframe to perform preprocessing operations

    Returns
    -------
    Dataframe
        pandas.DataFrame

    """
    try:
        # add all the information from the dataframe
        result = [ignore_and_return_result(add_all_info(x), ['pub_date']) for x in tqdm(data_frame['ID'])]

        # concat the dataframes
        data_frame = pd.concat([data_frame, pd.DataFrame(result)], axis=1)
        
        # return the dataframe
        return data_frame
    except:
        return pd.DataFrame()


if __name__ == '__main__':
    # read the data
    data = data_load('altmetrics_j2014_full.csv')

    # eliminate the articles that are published prior to 2014
    data = eliminate_row_by_pubdate(data)

    # process the dataframe
    data = data_processing(data)

    # export the data to a csv file
    data.to_csv('altmetrics_j2014_full_alpha.csv')

    # print the head of the
    #print(data.head())

    # print the number of NA's in the DOI column
    #print(data_prepare()['DOI'].isnull().sum().sum())
else:
    print('ERR: unable to run the script')
    sys.exit(0)

