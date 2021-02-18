#!/usr/bin/env python3
"""task 0"""


import tensorflow.keras as K
import tensorflow as tf


def preprocess_data(X, Y):
    """
    fonction de processe
    :param X:ndarray
    :param Y:ndarray
    """
    X1 = K.applications.resnet50.preprocess_input(X)
    Y1 = K.utils.to_categorical(Y, 10)
    return X1, Y1


if __name__ == "__main__":
    """ main program """
    (x_tr, y_tr), (XX, YY) = K.datasets.cifar10.load_data()
    x_tr, y_tr = preprocess_data(x_tr, y_tr)
    XX, YY = preprocess_data(XX, YY)
    entree = K.Input(shape=(224, 224, 3))
    fnl = K.applications.ResNet50(include_top=False,
                                  weights="imagenet",
                                  input_tensor=entree,
                                  pooling=None)
    for lyr in fnl.layers[:-10]:
        """ freezing """
        lyr.trainable = False
    model = K.models.Sequential()
    model.add(K.layers.Lambda(lambda image: tf.image.resize(image,
                                                            (224, 224))))
    atc = 'relu'
    model.add(fnl)
    model.add(K.layers.Flatten())
    model.add(K.layers.BatchNormalization())
    model.add(K.layers.Dense(256, activation=atc))
    model.add(K.layers.Dropout(0.5))
    model.add(K.layers.BatchNormalization())
    model.add(K.layers.Dense(128, activation=atc))
    model.add(K.layers.Dropout(0.5))
    model.add(K.layers.BatchNormalization())
    model.add(K.layers.Dense(64, activation=atc))
    model.add(K.layers.Dropout(0.5))
    model.add(K.layers.BatchNormalization())
    model.add(K.layers.Dense(10, activation='softmax'))

    callbaks = K.callbacks.ModelCheckpoint(filepath="cifar10.h5",
                                           monitor="val_acc",
                                           verbose=0,
                                           mode="max",
                                           save_best_only=True)
    model.compile(loss='categorical_crossentropy',
                  optimizer=K.optimizers.RMSprop(lr=2e-5),
                  metrics=['accuracy'])
    hist = model.fit(x_tr, y_tr, batch_size=32, epochs=10, verbose=1,
                     validation_data=(XX, YY), callbacks=[callbaks])
    """ saving model """
    model.summary()
    model.save('cifar10.h5')
