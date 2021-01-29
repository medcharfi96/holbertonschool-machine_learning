#!/usr/bin/env python3
""" task 6 """
import tensorflow.keras as K


def train_model(network, data, labels, batch_size,
                epochs, validation_data=None,
                early_stopping=False, patience=0,
                learning_rate_decay=False, alpha=0.1,
                decay_rate=1, verbose=True, shuffle=False):
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
    def scheduler(epoch):
        """
        ay 3asba
        :param epoch:
        """
        return alpha / (1 + decay_rate * epoch)
    test = []
    if early_stopping is True:
        wakaf = K.callbacks.EarlyStopping(monitor='val_loss',
                                          patience=patience)
        test.append(wakaf)
    if (learning_rate_decay and validation_data) is True:
        zab = K.callbacks.LearningRateScheduler(scheduler,
                                                verbose=1)
        test.append(zab)
    history = network.fit(x=data, y=labels,
                          callbacks=test,
                          epochs=epochs,
                          batch_size=batch_size,
                          validation_data=validation_data,
                          verbose=verbose,
                          shuffle=shuffle)
    return history
