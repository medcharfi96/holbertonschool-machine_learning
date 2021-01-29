#!/usr/bin/env python3
""" task 6 """
import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None, early_stopping=False,
                patience=0, verbose=True, shuffle=False):
    """
    zeb
    :param network:
    :param data:
    :param labels:
    :param batch_size:
    :param epochs:
    :param validation_data:
    :param early_stopping:
    :param patience:
    :param verbose:
    :param shuffle:
    """
    test = []
    if validation_data is True:
        if early_stopping is True:
            early_stop = K.callbacks.EarlyStopping(monitor='val_loss',
                                                   patience=patience,
                                                   verbose=verbose)
            test.append(early_stop)
    h = network.fit(x=data, y=labels,
                    epochs=epochs,
                    batch_size=batch_size,
                    validation_data=validation_data,
                    shuffle=shuffle,
                    verbose=verbose,
                    callbacks=test)
    return h
