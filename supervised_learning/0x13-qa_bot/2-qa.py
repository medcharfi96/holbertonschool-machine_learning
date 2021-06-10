#!/usr/bin/env python3
""" task 2 """


question_answer = __import__('0-qa').question_answer


def answer_loop(reference):
    """
    fonction de reponse  au text
    :param reference:
    """

    cases = ['exit', 'goodbye', 'bye']

    while True:
        question = input('Q: ')
        question = question.lower()

        if question in cases:
            print('A: Goodbye')
            break
        else:
            answer = question_answer(question, reference)
            if answer is None or answer == '':
                print('A: Sorry, I do not understand your question.')
            else:
                print('A: {}'.format(answer))
