# This Source Code Form is subject to the terms of the MPL
# License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/akhilpandey95/altpred/blob/master/LICENSE.

import json
import requests
from collections import defaultdict

# add title of the scholarly paper
def add_title(alt_id):
    try:
        response = requests.get("https://api.altmetric.com/v1/id/" + str(alt_id))
        if 'title' in dict(json.loads(response.content)):
            return dict(json.loads(response.content))['title']
    except:
        return ''

# add abstract of the scholarly paper
def add_abs(alt_id):
    try:
        response = requests.get("https://api.altmetric.com/v1/id/" + str(alt_id))
        if 'abstract' in dict(json.loads(response.content)):
            return dict(json.loads(response.content))['abstract']
    except:
        return ''

# add author count of the scholarly paper
def add_author_count(alt_id):
    try:
        response = requests.get("https://api.altmetric.com/v1/id/" + str(alt_id))
        return len(dict(json.loads(response.content))['authors'])
    except:
        return ''

# add doi of the scholarly paper
def add_doi(alt_id):
    try:
        response = requests.get("https://api.altmetric.com/v1/id/" + str(alt_id))
        return dict(json.loads(response.content))['doi']
    except:
        return ''

# add author information
def add_author_name(alt_id):
    try:
        response = requests.get("https://api.altmetric.com/v1/id/" + str(alt_id))
        return dict(json.loads(response.content))['authors']
    except:
        return ''
    
# add author information
def add_all_info(alt_id):
    # create the dict
    result = defaultdict(dict)
    try:
        # make the request
        response = requests.get("https://api.altmetric.com/v1/id/" + str(alt_id))
        
        # add the values to the dict
        if 'authors' in dict(json.loads(response.content)):
            result['author_count'] = len(dict(json.loads(response.content))['authors'])
            result['authors'] = ', '.join(dict(json.loads(response.content))['authors'])
        else:
            result['author_count'] = ''
            result['authors'] = ''
        
         # add the values to the dict
        if 'doi' in dict(json.loads(response.content)):
            result['doi'] = dict(json.loads(response.content))['doi']
        else:
            result['doi'] = ''
        
        # add the abstract
        if 'abstract' in dict(json.loads(response.content)):
            result['abstract'] = dict(json.loads(response.content))['abstract']
        else:
            result['abstract'] = ''
        
        # add the title of the article
        if 'title' in dict(json.loads(response.content)):
            result['title'] =  dict(json.loads(response.content))['title']
        else:
            result['title'] = ''
        
        # return the result
        return result
    except:
        return result
