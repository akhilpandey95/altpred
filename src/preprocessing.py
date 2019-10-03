# This Source Code Form is subject to the terms of the MIT
# License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/akhilpandey95/altpred/blob/master/LICENSE.

import re
import spacy
import string
import gensim
import numpy as np
import pandas as pd
from tqdm import tqdm
from nltk.corpus import stopwords
from gensim.corpora import Dictionary
from gensim.models.ldamulticore import LdaMulticore
from nltk.stem.wordnet import WordNetLemmatizer

# Recurrent network (GRU) for predicting twitter count
class LDA():
    """
    Class object for predicting if for a given
    scholarly paper there is a change in attention
    it receives on twitter

    Parameters
    ----------
    No arguments

    Returns
    -------
    LDA Model
        gensim.models.ldamodel.LdaModel

    """
    # function for preparing the X for topic modeling
    def __init__(self):
        """
        Preprocess the data and clean it

        Parameters
        ----------
        No arguments

        Returns
        -------
        Nothing
            None

        """
        # super class the keras model
        super(LDA, self).__init__()

        # collect the stopwords from nltk
        self.stop_words = set(stopwords.words('english'))

        # exlcude some words
        self.exclude = set(string.punctuation)

        # prepare the wordnet lemmatizer
        self.lemma = WordNetLemmatizer()

    # function for normalizing the input
    def normalize(self, X):
        """
        Clean the given corpus and normalize it consequently

        Parameters
        ----------
        arg1 | X: numpy.ndarray
            An array consisting of strings/documents

        Returns
        -------
        Array
            numpy.ndarray

        """
        try:
            # check and remove stop words from input
            stop_free = ' '.join([i for i in X.lower().split() if i not in self.stop_words])

            # check for punctuations
            punc_free = ''.join(ch for ch in stop_free if ch not in self.exclude)

            # normalize the inputs
            normalized = ' '.join(self.lemma.lemmatize(word) for word in punc_free.split())

            # return the normalized input
            return normalized
        except:
            # return an empty array
            return np.zeros(len(X))

    # function for training the LDA
    def train(self, X, topics, passes):
        """
        Train on the given corpus

        Parameters
        ----------
        arg1 | X: numpy.ndarray
            Normalized input to be used for the LDA model
        arg2 | topics: int
            Number of topics to be used for the LDA model
        arg3 | passes: int
            Number of passes to be used for the LDA model

        Returns
        -------
        LDA Model
            gensim.model.ldamodel

        """
        try:
            # build the corpora dictionary
            categories = Dictionary(X)

            # obtain the document topic matrix
            topic_matrix = [categories.doc2bow(category) for category in tqdm(X)]

            # train on the matrix
            model = LdaMulticore(topic_matrix, workers=5, num_topics=topics, id2word=categories, passes=passes)

            # return the model
            return model
        except:
            # return an empty gensim model
            return gensim.models.ldamodel.LdaModel
