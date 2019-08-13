# This Source Code Form is subject to the terms of the MIT
# License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/akhilpandey95/reproducibility/blob/master/LICENSE.

import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score

# function for evaluating the model and reporting stats
def evaluate(model, **data):
    """
    Fit the neural network model
    Parameters
    ----------
    arg1 | model: keras.model.Model
        A trained keras neural network model
    arg2 | **data: variable function arguments
        The variable argument used for pulling the training or test data
    Returns
    -------
    Array
        numpy.ndarray
    """
    try:
        # evaluate the model and print the training stats
        evaluation = model.evaluate(data['x_train'], data['y_train'])

        # return the model
        return evaluation
    except:
        return np.zeros(2)

# function for printing metrics for the model
def metrics(model, **data):
    """
    Predict the test samples and return the metrics for the model
    Parameters
    ----------
    arg1 | model: keras.model.Model
        A trained keras neural network model
    arg2 | option: string
        An optional flag for printing either classification
        or regression metrics. Pass the value 'r' to the option
        flag if you desire to print regression, else the function
        returns classification metrics by default
    arg3 | **data: variable function arguments
        The variable argument used for pulling the training or test data
    Returns
    -------
    List
        [float, float, float, float]
    """
    try:
        # predict the model
        y_pred= model.predict(data['x_test'])

        # predict the values
        y_pred = (y_pred > 0.5)

        # test accuracy
        acc = accuracy_score(data['y_test'], y_pred)

        # precision
        prec = precision_score(data['y_test'], y_pred)

        # recall
        rec = recall_score(data['y_test'], y_pred)

        # f-1
        f1 = f1_score(data['y_test'], y_pred)

        # return the r-squared value
        return [acc, prec, rec, f1]
    except:
        return np.zeros(4)
