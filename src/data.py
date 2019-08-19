# This Source Code Form is subject to the terms of the MIT
# License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/akhilpandey95/altpred/blob/master/LICENSE.

import numpy as np
import pandas as pd
from tqdm import tqdm
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.preprocessing.text import Tokenizer

# function for computing sigmoid of a value
def sigmoid(value, derivative=False):
    """
    Return the sigmoid of a numeric value

    Parameters
    ----------
    arg1 | value: int
        The numeric value intended to convert into a continuos range

    Returns
    -------
    Float
        float

    """
    try:
        # compute the sigmoid
        result = 1. / (1. + np.exp(-x))

        # check if derivative is required
        if derivative:
            # return the sigmoid
            return result * (1. - result)

        # return the sigmoid
        return result
    except:
        # return zero
        return np.zeros(1)[0]

# function for processing the dataset
def data_processing(file_path):
    """
    Process the dataset and prepare it for using it against the neural network model

    Parameters
    ----------
    arg1 | file_path: str
        The file path indicating the location of the dataset

    Returns
    -------
    Dataframe
        pandas.DataFrame

    """
    try:
        # read the dataset
        data = pd.read_csv(file_path, low_memory=False)

        # get a sample of the data
        data = data.sample(frac=0.25, random_state=2019).reset_index(drop=True)

        # add a column
        data = data.assign(exp_3_sigmoid = list(map(sigmoid, tqdm(data['twitter_count_y18']))))

        # drop the columns unecessary
        data = data.drop(columns=['Unnamed: 0'])

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
    # try:
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
    # except:
    #     return np.zeros(20).reshape(2, 10), np.zeros(10), np.zeros(1)[0], np.zeros(1)[0]
