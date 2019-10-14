# This Source Code Form is subject to the terms of the MIT
# License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/akhilpandey95/altpred/blob/master/LICENSE.

import sys
from models import *
from evaluation import evaluate, clf_metrics
from data import data_processing, prepare_word_embeddings
from sklearn.model_selection import train_test_split
from collections import Counter
from tensorflow.keras.utils import plot_model

if __name__ == '__main__':
    # load the dataset
    data = data_processing('altmetrics_j2014_full_gamma.csv', 'binary')
    #data = data_processing('altmetrics_j2014_full_gamma.csv', 'binary-delta')

    # prepare the X, Y
    X, Y, max_words, max_len = prepare_word_embeddings(data, 'pub_subjects', 'target')
    print(Counter(data['target']))

    # build the train and test samples
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.35)

    # build the model
    classifier = AltpredTwitterGRU(max_words, max_len)
    classifier = AltpredTwitterLSTM(max_words, max_len)
    #classifier = AltpredTwitterBiDirLSTM(max_words, max_len)

    plot_model(classifier, to_file='altpred-exp1-GRU.png', dpi=300)

    # train the model
    classifier = classifier.train(5, 256, X_train, Y_train, stopping=False)

    # evaluate and print the training stats
    model_evaluation = evaluate(classifier, 'train', x_train=X_train, y_train=Y_train)

    # print training metrics
    print('Training Loss:', model_evaluation[0])
    print('Training Accuracy:', model_evaluation[1])

    # print the test set metrcs [acc, prec, recall, f1]
    model_evaluation = clf_metrics(classifier, x_test=X_test, y_test=Y_test)

    # test accuracy
    print('Test accuracy:', model_evaluation[0])

    # precision
    print('Precision:', model_evaluation[1])

    # recall
    print('Recall:', model_evaluation[2])

    # f1
    print('F-1:', model_evaluation[3])
else:
    print('ERR: unable to run the script')
    sys.exit(0)
