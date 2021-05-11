#!/usr/bin/env python3
""" task 1 """


from sklearn.feature_extraction.text import TfidfVectorizer


def tf_idf(sentences, vocab=None):
    """
    creation de tf-idf
    :param sentences:list
    :param vocab: lists
    """

    vectorizer = TfidfVectorizer(vocabulary=vocab)
    X = vectorizer.fit_transform(sentences)

    feat = vectorizer.get_feature_names()

    embedding = X.toarray()

    return embedding, feat
