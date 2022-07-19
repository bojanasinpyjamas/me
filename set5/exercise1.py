# -*- coding: UTF-8 -*-

from random import randint
import requests

"""REFACTORING

Refactoring is the process of making your code better. You are usually looking 
to make it more readable or easier to maintain. Usually you'll do this by 
pulling out bits of code that encapsualte one idea, especially if that idea is 
used in several places.

We've talked already about 
    ↱red→green→refactor↴
    ↜←←←←←←←←←←←←←←←←←←↩

Where red means make sure the test fails if you haven't done anything, green 
means make the test pass, however you can, now this is the reafactor part.

The function below works fine, but it's long and hard to read. Identify the 
parts that are repeated, and pull them out into their own functions. I've made 
that easier for you by making the function stubs for the bits you need to do.

Modify this function, don't write a whole new one.
"""


def wordy_pyramid():
    numbers = list(range(3, 21, 2)) + list(range(20, 3, -2))
    pyramid_list = list_of_words_with_lengths(numbers)
    return pyramid_list


def get_a_word_of_length_n(length):
    url = f"https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={length}"
    r = requests.get(url)
    if r.status_code is 200:
        word = r.text
        return word


def list_of_words_with_lengths(list_of_lengths):
    words = []
    for length in list_of_lengths:
        words.append(get_a_word_of_length_n(length))
    return words


if __name__ == "__main__":
    pyramid = wordy_pyramid()
    for word in pyramid:
        print(word)
