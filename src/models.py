# This Source Code Form is subject to the terms of the MIT
# License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/akhilpandey95/altpred/blob/master/LICENSE.

import tensorflow.keras as keras
from tensorflow.keras import Model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense
from tensorflow.keras.layers import GRU, LSTM, SimpleRNN, Bidirectional

# Recurrent network (GRU) for predicting twitter count
class AltpredTwitterGRU(Model):
    """
    Class object for predicting if for a given
    scholarly paper there is a change in attention
    it receives on twitter

    Parameters
    ----------
    No arguments

    Returns
    -------
    Neural Network Model
        keras.model.Model

    """
    # function for preparing the X & Y for the dataset
    def __init__(self, max_words, max_len):
        """
        Build the GRU neural network model and compile it

        Parameters
        ----------
        No arguments

        Returns
        -------
        Nothing
            None

        """
        # super class the keras model
        super(AltpredTwitterGRU, self).__init__()

        # create the model
        self.model = Sequential()

        # add the Embedding layer with 64 neurons, relu activation
        self.model.add(Embedding(max_words, 64, input_length=max_len))

        # add the first GRU layer with 32 units
        self.model.add(GRU(128, return_sequences=True))

        # add the first GRU layer with 16 units
        #self.model.add(GRU(64, return_sequences=True))

        # add the first GRU layer with 8 units
        #self.model.add(GRU(8, return_sequences=True))

        # add the fourth GRU layer with 4 units
        self.model.add(GRU(64))

        # add a simpleRNN layer with 64 units
        # self.model.add(SimpleRNN(64))

        # add the output layer containing the label
        self.model.add(Dense(1, activation='softmax'))

        # use the rmsprop optimizer
        self.rms = keras.optimizers.RMSprop(lr=0.001)

        # compile the model
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics =['accuracy'])

    # function for training the neural network model
    def train(self, epochs, batch_size, X_train, Y_train, stopping=True):
        """
        Fit the neural network model

        Parameters
        ----------
        arg1 | model: keras.model.Model
            A compiled keras neural network model to train
        arg2 | epochs: numpy.int32
            Number of epochs needed to train the model
        arg3 | batch_size: numpy.int32
            Batch size of the model
        arg4 | X_train: numpy.ndarray
            The training samples containing all the predictors
        arg5 | Y_train: numpy.ndarray
            The training samples containing values for the target variable
        arg6 | stopping: boolean
        A flag asserting if early stopping should or shouldn't be used for training

        Returns
        -------
        Neural Network Model
            keras.model.Model

        """
        try:
            if not stopping:
                # fit the model
                self.model.fit(X_train, Y_train, epochs=epochs, validation_split=0.2, batch_size=batch_size)
            else:
                # prepare for early stopping
                early_stopping = keras.callbacks.EarlyStopping(monitor='binary_crossentropy', min_delta=0,
                                                         patience=2, verbose=0, mode='auto',
                                                         baseline=None, restore_best_weights=False)
                # fit the model
                self.model.fit(X_train, Y_train, epochs=epochs, validation_split=0.2, batch_size=batch_size, callbacks=[early_stopping])

            # return the model
            return self.model
        except:
            return keras.models.Model()

# Recurrent network (LSTM) for predicting twitter count
class AltpredTwitterLSTM(Model):
    """
    Class object for predicting if for a given
    scholarly paper there is a change in attention
    it receives on twitter

    Parameters
    ----------
    No arguments

    Returns
    -------
    Neural Network Model
        keras.model.Model

    """
    # function for preparing the X & Y for the dataset
    def __init__(self, max_words, max_len):
        """
        Build the LSTM neural network model and compile it

        Parameters
        ----------
        No arguments

        Returns
        -------
        Nothing
            None

        """
        # super class the keras model
        super(AltpredTwitterLSTM, self).__init__()

        # create the model
        self.model = Sequential()

        # add the Embedding layer with 64 neurons, relu activation
        self.model.add(Embedding(max_words, 64, input_length=max_len))

        # add an LSTM layer with 64 units
        self.model.add(LSTM(256))

        # add the output layer containing the label
        self.model.add(Dense(1, activation='sigmoid'))

        # use the rmsprop optimizer
        self.rms = keras.optimizers.RMSprop(lr=0.001)

        # compile the model
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics =['accuracy'])

    # function for training the neural network model
    def train(self, epochs, batch_size, X_train, Y_train, stopping=True):
        """
        Fit the neural network model

        Parameters
        ----------
        arg1 | model: keras.model.Model
            A compiled keras neural network model to train
        arg2 | epochs: numpy.int32
            Number of epochs needed to train the model
        arg3 | batch_size: numpy.int32
            Batch size of the model
        arg4 | X_train: numpy.ndarray
            The training samples containing all the predictors
        arg5 | Y_train: numpy.ndarray
            The training samples containing values for the target variable
        arg6 | stopping: boolean
        A flag asserting if early stopping should or shouldn't be used for training

        Returns
        -------
        Neural Network Model
            keras.model.Model

        """
        try:
            if not stopping:
                # fit the model
                self.model.fit(X_train, Y_train, epochs=epochs, validation_split=0.2, batch_size=batch_size)
            else:
                # prepare for early stopping
                early_stopping = keras.callbacks.EarlyStopping(monitor='binary_crossentropy', min_delta=0,
                                                         patience=2, verbose=0, mode='auto',
                                                         baseline=None, restore_best_weights=False)
                # fit the model
                self.model.fit(X_train, Y_train, epochs=epochs, validation_split=0.2, batch_size=batch_size, callbacks=[early_stopping])

            # return the model
            return self.model
        except:
            return keras.models.Model()

# Recurrent network (bidirLSTM) for predicting twitter count
class AltpredTwitterBiDirLSTM(Model):
    """
    Class object for predicting if for a given
    scholarly paper there is a change in attention
    it receives on twitter

    Parameters
    ----------
    No arguments

    Returns
    -------
    Neural Network Model
        keras.model.Model

    """
    # function for preparing the X & Y for the dataset
    def __init__(self, max_words, max_len):
        """
        Build the LSTM neural network model and compile it

        Parameters
        ----------
        arg1 | problem: str
            A flag for creating models suitable for a classification
            or a regression problem

        Returns
        -------
        Nothing
            None

        """
        # super class the keras model
        super(AltpredTwitterBiDirLSTM, self).__init__()

        # create the model
        self.model = Sequential()

        # add the Embedding layer with 64 neurons, relu activation
        self.model.add(Embedding(max_words, 64, input_length=max_len))

        # add a Bidirectional LSTM layer with 64 units
        self.model.add(Bidirectional(LSTM(128, return_sequences=True)))

        # add a Bidirectional LSTM layer with 32 units
        self.model.add(Bidirectional(LSTM(32)))

        # add the output layer containing the label
        self.model.add(Dense(1, activation='softmax'))

        # use the rmsprop optimizer
        self.rms = keras.optimizers.RMSprop(lr=0.001)

        # compile the model
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics =['accuracy'])

    # function for training the neural network model
    def train(self, epochs, batch_size, X_train, Y_train, stopping=True):
        """
        Fit the neural network model

        Parameters
        ----------
        arg1 | model: keras.model.Model
            A compiled keras neural network model to train
        arg2 | epochs: numpy.int32
            Number of epochs needed to train the model
        arg3 | batch_size: numpy.int32
            Batch size of the model
        arg4 | X_train: numpy.ndarray
            The training samples containing all the predictors
        arg5 | Y_train: numpy.ndarray
            The training samples containing values for the target variable
        arg6 | stopping: boolean
        A flag asserting if early stopping should or shouldn't be used for training

        Returns
        -------
        Neural Network Model
            keras.model.Model

        """
        try:
            if not stopping:
                # fit the model
                self.model.fit(X_train, Y_train, epochs=epochs, validation_split=0.2, batch_size=batch_size)
            else:
                # prepare for early stopping
                early_stopping = keras.callbacks.EarlyStopping(monitor='binary_crossentropy', min_delta=0,
                                                         patience=2, verbose=0, mode='auto',
                                                         baseline=None, restore_best_weights=False)
                # fit the model
                self.model.fit(X_train, Y_train, epochs=epochs, validation_split=0.2, batch_size=batch_size, callbacks=[early_stopping])

            # return the model
            return self.model
        except:
            return keras.models.Model()
