#!/usr/bin/env python3
""" task 0 """


from sklearn.feature_extraction.text import CountVectorizer


def bag_of_words(sentences, vocab=None):
    """
    creation de  bag of word
    :param sentences:list
    :param vocab:list
    """

    vectorizer = CountVectorizer(vocabulary=vocab)
    X = vectorizer.fit_transform(sentences)
    embeddings = X.toarray()
    feat = vectorizer.get_feature_names()

    return embeddings, feat
