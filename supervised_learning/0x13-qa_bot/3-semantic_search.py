#!/usr/bin/env python3
""" task 3 """


import numpy as np
import os
import tensorflow_hub as hub


def semantic_search(corpus_path, sentence):
    """
    fonction de performer la recherche sematique
    :param corpus_path:
    :param sentence:
    """

    doc = [sentence]

    for f in os.listdir(corpus_path):
        if not f.endswith('.md'):
            continue
        with open(corpus_path + '/' + f, 'r', encoding='utf-8') as file:
            doc.append(file.read())

    embed = hub.load(
        'https://tfhub.dev/google/universal-sentence-encoder-large/5')
    embeddings = embed(doc)

    sim = np.inner(embeddings, embeddings)
    clos = np.argmax(sim[0, 1:])

    return doc[clos + 1]
