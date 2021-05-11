#!/usr/bin/env python3
""" task 2 """


from gensim.models import Word2Vec


def word2vec_model(sentences, size=100, min_count=5,
                   window=5, negative=5, cbow=True,
                   iterations=5, seed=0, workers=1):
    """
    creation de word2Vec modele
    :param sentences: list
    :param size:int
    :param min_count: int
    :param window: int
    :param negative: int
    :param cbow: bool
    :param iterations: int
    :param seed:int
    :param workers:int
    :return:
    """

    modele = Word2Vec(sentences=sentences,
                      min_count=min_count,
                      iter=iterations,
                      size=size,
                      sg=cbow,
                      seed=seed,
                      negative=negative)
    modele.train(sentences=sentences,
                 total_examples=modele.corpus_count,
                 epochs=modele.epochs)
    return modele
