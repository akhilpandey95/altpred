# This Source Code Form is subject to the terms of the MIT
# License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/akhilpandey95/altpred/blob/master/LICENSE.

import sys
import json
import certifi
import urllib3
import requests
import numpy as np
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup as BS
from collections import defaultdict

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

# function for downloading the content from a URI
def obtain_content(uri):
    """
    Return the decoded response after making a get request to the URI

    Parameters
    ----------
    arg1 | uri: str
        Index number that holds information for a class

    Returns
    -------
    String
        str

    """
    try:
        # create a urllib object
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

        # establish a connection and make a GET request to the URI
        res = http.request('GET', uri)

        # decode the value
        res = res.data.decode('utf-8')

        # return the decoded response
        return res
    except:
        return None

# add title of the scholarly paper
def soupify(year):
    """
    Prepare a soup object by storing information all the articles in a list

    Parameters
    ----------
    arg1 | year: int
        The year from which we want to extrapolate information

    Returns
    -------
    Dictionary
        collections.defaultdict

    """
    try:
        # create the url string
        url = 'https://www.altmetric.com/top100/'

        # obtain the content for a given year
        html = obtain_content(url + str(year))

        # create a beautiful soup object
        soup = BS(html, 'html.parser')

        # return the soup
        return soup.find_all('article')
    except:
        return None

# function for extracting article information from the soup object
def extract_article_information_year_2014(soup):
    """
    Collect article information from the soup object

    Parameters
    ----------
    arg1 | soup: bs4.element.Tag
        The specific article we are looking to extrapolte information

    Returns
    -------
    Dictionary
        collections.defaultdict

    """
    try:
        # get the soup object
        data = defaultdict(dict)

        # add the article rank
        data['ranking'] = int(soup.find('div', class_='ranking').text)

        # add the altmetric id
        data['altmetric_id'] = int(soup.find('div', class_='metrics').find('a')['href'].split('=')[1])

        # add the DOI of the article
        data['doi'] = soup.find('h2').find('a')['href']

        # add the title of the article
        data['title'] = soup.find('h2').find('a').getText()

        # add the author information of the article
        data['authors'] = soup.find('div', class_='subtitle').text.strip()

        # add the journal name of the article
        data['journal'] = [x.find_next('td').text for x in \
                        soup.find('div', class_='details').find('table', class_='article-data') \
                        .find_all('th') if 'Journal' in x.text][0]

        # add the tweet count of the article
        data['tweet_count'] = int([x.next_sibling.text.split(' ') \
                    for x in \
                    soup.find('div', class_='mentions').find_all('dt') if 'twitter' in x.text][0][0])

        # return the data
        return data
    except:
        return None

if __name__ == '__main__':
    # test if the we are able to extract information for the 1st article from 2014 list
    print(extract_article_information_year_2014(soupify(2014)[0]))
else:
    sys.exit(0)
