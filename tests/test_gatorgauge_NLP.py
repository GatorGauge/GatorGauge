import gensim
import pytest
import refl_gensim

"""tests the NLP/gensim"""

def test_create_tokens_none_repeat():
    list_responses = [['I am testing'], ['this is a test'], ['make my tokens']]
    check = refl_gensim.create_tokens(list_responses)
    print(check)
    assert check == [['testing'], ['test'], ['make', 'tokens']]


def test_create_tokens_repeated():
    list_responses = [['I am testing'], ['testing testing testing'], ['make my tokens']]
    check = refl_gensim.create_tokens(list_responses)
    print(check)
    assert check == [['testing'], ['testing', 'testing', 'testing'], ['make', 'tokens']]


def test_dictionary_create_repeat():
    tokens = [
        ['testing'], [
            'testing', 'testing', 'testing'], [
            'make', 'tokens']]
    dictionary = refl_gensim.dictionary_create(tokens)
    corp = [dictionary.doc2bow(token) for token in tokens]
    print(corp)
    assert corp == [[(0, 1)], [(0, 3)], [(1, 1), (2, 1)]]
