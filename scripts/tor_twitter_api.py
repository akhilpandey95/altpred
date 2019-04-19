# This Source Code Form is subject to the terms of the MPL
# License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/akhilpandey95/altpred/blob/master/LICENSE.

import os
import requests
from torrequest import TorRequest

# function for assigning new IP address
def assign_new_ip(text=False):
    """
    Reset the identity using TorRequest

    Parameters
    ----------
    arg1 [OPTIONAL]| text: bool
        A boolean flag to return the IP address tuple (old, morphed)

    Returns
    -------
    boolean
        True/False

    """

    try:
        # pass the hashed password
        req = TorRequest(password='16:A30187C3D040273560006F14F4F43B8F3718D2D8EE9AE3104412BA83EC')

        # return the ip address
        normal_identity = requests.get('http://ipecho.net/plain')

        # reset the identity using Tor
        req.reset_identity()

        # make a request now
        morphed_identity = req.get('http://ipecho.net/plain')

        # return the status depending on the flag
        if morphed_identity != normal_identity:
            if text == True:
                # return the ip address pairs as a tuple
                return (normal_identity.text, morphed_identity.text)
            else:
                return True
        else:
            # return just the status
            return False
    except:
        return False


# function for downloading the tweet from a given url
def get_tweet(tweet_url):
    """
    Return the text of the tweet from the url

    Parameters
    ----------
    arg1 | tweet_url: str
        A boolean flag to return the IP address tuple (old, morphed)

    Returns
    -------
    str
        text of the tweet

    """
    try:
        # return the status
        return True
    except:
        return False

if __name__ == '__main__':
    print(assign_new_ip(text=True))
else:
    sys.exit(0)

