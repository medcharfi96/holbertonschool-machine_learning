#!/usr/bin/env python3
""" task 4"""


from gensim.models import FastText


def fasttext_model(sentences, size=100, min_count=5, negative=5,
                   window=5, cbow=True, iterations=5, seed=0, workers=1):
    """
    creation de fastText
    :param sentences: lint
    :param size:int
    :param min_count:int
    :param negative:int
    :param window: int
    :param cbow: bool
    :param iterations:int
    :param seed: int
    :param workers: int
    """

    model = FastText(sentences,
                     size=size,
                     min_count=min_count,
                     window=window,
                     negative=negative,
                     sg=cbow,
                     seed=seed,
                     workers=workers)

    model.train(sentences,
                total_examples=model.corpus_count,
                epochs=iterations)

    return model
