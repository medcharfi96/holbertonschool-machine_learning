#!/usr/bin/env python3
""" task 3 """

from gensim.models import Word2Vec


def gensim_to_keras(model):
    """
    conversion vers keras embedding
    :param model: model word2Vec
    """
    return model.wv.get_keras_embedding(train_embeddings=True)
