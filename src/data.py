# This Source Code Form is subject to the terms of the MIT
# License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/akhilpandey95/altpred/blob/master/LICENSE.

import numpy as np
import pandas as pd
from tqdm import tqdm
from ast import literal_eval
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.preprocessing.text import Tokenizer

# function for processing the dataset
def data_processing(file_path, target):
    """
    Process the dataset and prepare it for using it against the neural network model

    Parameters
    ----------
    arg1 | file_path: str
        The file path indicating the location of the dataset
    arg2 | target: str
        The type of target variable going to be used for the experiment

    Returns
    -------
    Dataframe
        pandas.DataFrame

    """
    try:
        # read the dataset
        data = pd.read_csv(file_path, low_memory=False)

        # get a sample of the data
        data = data.sample(frac=0.25, random_state=2019)

        # reset the index for the dataframe
        data = data.reset_index(drop=True)

        # drop the columns unecessary
        data = data.drop(columns=['Unnamed: 0'])

        # remove the entries which don't have a title
        data = data.loc[data.title.apply(type) != float].reset_index(drop=True)

        # convert the pub_subjects column into a list
        data = data.assign(pub_subjects = list(map(lambda x: ' '.join(literal_eval(x)), tqdm(data['pub_subjects']))))

        # check the experiment and create the target variable accordingly
        if target == 'binary':
            # create the target variable for the binary experiment
            data = data.assign(target = list(map(lambda x, y: 0 if x == y else 1, tqdm(data['TWITTER_ACCOUNTS']), tqdm(data['twitter_count_y18']))))
        else:
            # create the target variable for multi class experiment
            data = data.assign(target = list(map(lambda x, y: 0 if x > y else 2 if x < y else 1, tqdm(data['TWIITER_ACCOUNTS']), tqdm(data['twitter_count_y18']))))

        # return the dataframe
        return data
    except:
        return pd.DataFrame()

# function for preparing word embeddings
def prepare_word_embeddings(data, X, Y):
    """
    Prepare the word embeddings for the abstracts of every scholarly paper

    Parameters
    ----------
    arg1 | data: pandas.DataFrame
        A dataframe consisting of necessary columns for extracting abstract
        and the target variable
    arg2 | X: numpy.ndarray
        An array consisting of texts from the dataframe that would be converted
        into word embeddings
    arg3 | Y: numpy.ndarray
        An array consisting of the label values for the target variable

    Returns
    -------
    Array, Array, Number, Number
        numpy.ndarray, numpy.ndarray, int, int

    """
    try:
        # find the maximum words and maximum length for the given dataset
        max_words = max(list(map(lambda x: len(x.split()), tqdm(data[X]))))

        # find max length of the text for the given dataset
        max_len = max(list(map(len, tqdm(data[X]))))

        # init the tokenizer class object
        tok = Tokenizer(num_words=max_words)

        # fit the tokenizer on the text data
        tok.fit_on_texts(data[X])

        # generate the sequences
        sequences = tok.texts_to_sequences(data[X])

        # obtain the sequence matrix
        X = sequence.pad_sequences(sequences, maxlen=max_len)

        # the target variable
        Y = data[Y].values

        # reshape the target variable
        Y = Y.reshape(-1, 1)

        # return the dataframe
        return X, Y, max_words, max_len
    except:
        return np.zeros(20).reshape(2, 10),np.zeros(10),np.zeros(1)[0],np.zeros(1)[0]
