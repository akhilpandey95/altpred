# This Source Code Form is subject to the terms of the MPL
# License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/akhilpandey95/altpred/blob/master/LICENSE.

import sys
import pandas as pd
from tqdm import tqdm
from altmetric_api import add_all_info

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
        data = data.drop(columns=['DOI', 'PMID', 'ARXIV_ID', 'HANDLE', 'FACEBOOK_WALLS', 'BLOGS', 'GPLUS_ACCOUNTS', 'NEWS_OUTLETS'])

        # return the dataframe
        return data
    except:
        return pd.DataFrame()

# function for processing the dataset
def data_processing(data_frame):
    """
    The 

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
        result = [add_all_info(x) for x in tqdm(data_frame['ID'])]

        # concat the dataframes
        data_frame = pd.concat([data_frame, pd.DataFrame(result)], axis=1)
        
        # return the dataframe
        return data_frame
    except:
        return pd.DataFrame()


if __name__ == '__main__':
    # read the data
    data = data_load('altmetrics_j2014_full.csv')

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

