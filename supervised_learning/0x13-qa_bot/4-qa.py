#!/usr/bin/env python3
""" task 4"""


qa = __import__('0-qa').question_answer
semantic_search = __import__('3-semantic_search').semantic_search


def question_answer(coprus_path):
    """
    fonction de reponse au question
    :param coprus_path:
    """

    cases = ['exit', 'goodbye', 'bye']

    while True:
        question = input('Q: ')
        question = question.lower()

        if question in cases:
            print('A: Goodbye')
            break
        else:
            reference = semantic_search(coprus_path, question)
            answer = qa(question, reference)
            if answer is None or answer == '':
                print('A: Sorry, I do not understand your question.')
            else:
                print('A: {}'.format(answer))
