# Michael Hart
# CIS256 Spring 2026
# Exercise Assignment 4

# Import methods from guess_the_word
# Import the words, the is_word_in_list function, and the process_guess function.
from guess_the_word import is_word_in_list, process_guess

# Tests if the words are in the list.
def test_is_word_in_list():
    assert is_word_in_list("taco") == True
    assert is_word_in_list("kumquat") == False

# Tests to make sure correct and incorrect
# answers are being processed properly.
def test_correct_incorrect_process():
    # The list here won't be tested, just the result of the
    # process_guess function.
    indexes_guessed = []
    # Word from the pre-defined list.
    word_chosen = "tower"
    assert process_guess(indexes_guessed, "w", word_chosen) == True
    assert process_guess(indexes_guessed, "q", word_chosen) == False
