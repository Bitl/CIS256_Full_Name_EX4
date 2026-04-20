# Michael Hart
# CIS256 Spring 2026
# Exercise Assignment 4

# Import the random class.
import random

# The list of words. Declared globally.
words = ["taco", "tower", "ketchup",
         "hamburger", "tomodachi", "cheddar",
         "chicken", "boxes", "shoes"]

# A method that checks whether or not a word is in the list.
def is_word_in_list(word):
    for curword in words:
        if curword == word:
            return True

    return False

# Checks if the letter is in the word string.
def word_has_letter(suggested_letter, word):
    for letter in word:
        if letter == suggested_letter:
            return True

    return False

# Display any letters that we guessed properly.
def display_letters(indexes_guessed, word):
    # Initalize the index variable with an invalid index.
    cur_index = -1
    final_letter_string = ""
    for letter in word:
        # Increment index
        cur_index += 1
        # If the letter has already been uncovered, print it out in uppercase.
        # If not, only show an underscore (_).
        # As the loop goes through, build the string by adding it with a space.
        if cur_index in indexes_guessed:
            final_letter_string += letter.upper() + " "
        else:
            final_letter_string += "_ "

    return final_letter_string

# Checks if a guess/index exists in the indexes_guessed list.
def index_exists(indexes_guessed, index):
    for cur_index in indexes_guessed:
        if cur_index == index:
            return True

    return False

# "Unlock" a letter in a word (add the letter to the "indexes_guessed" list).
def unlock_letter(indexes_guessed, index):
    # Make sure the index doesn't already exist.
    if not index_exists(indexes_guessed, index):
        indexes_guessed.append(index)

# Process a guess and check if it's true or false.
# If it's true, add all instances of the correct letter to the "indexes_guessed"
# list and return true.
# If not, just return false.
def process_guess(indexes_guessed, suggested_letter, word):
    if word_has_letter(suggested_letter, word):
        # Initalize the index variable with an invalid index.
        cur_index = -1
        for letter in word:
            # Increment index
            cur_index += 1
            # If the letter matches, add its index to the list.
            if letter == suggested_letter:
                # Attempt to unlock the letter.
                unlock_letter(indexes_guessed, cur_index)
        return True

    return False

# Check a guess and see if the suggested letter exists in the "indexes_guessed"
# list. Return true if it does.
def check_guess_letter_exists(indexes_guessed, suggested_letter, word):
    if word_has_letter(suggested_letter, word):
        # Initalize the index variable with an invalid index.
        cur_index = -1
        for letter in word:
            # Increment index
            cur_index += 1
            if letter == suggested_letter:
                # Check if the letter exists.
                if index_exists(indexes_guessed, cur_index):
                    return True

    return False

# Unlock all letters in a word.
# Used for the lose condition.
def unlock_all(indexes_guessed, word):
    # Initalize the index variable with an invalid index.
    cur_index = -1
    for letter in word:
        # Increment index
        cur_index += 1
        # Instantly unlock the letter.
        unlock_letter(indexes_guessed, cur_index)

# Return a number of attempts based on the character count of the word,
# plus 2 additional attempts for fairness.
def calculate_attempts(word):
    attempts = 2
    
    for letter in word:
        attempts += 1

    return attempts

#
def game_main():
    global words
    word_chosen = random.choice(words)
    indexes_guessed = []
    attempts = calculate_attempts(word_chosen)

    while True:
        print("------------------------------------")
        
        # Process win/lose condition before displaying the dialog.
        if len(indexes_guessed) == len(word_chosen):
            # Display the completed word puzzle, then display a congratulatory message.
            print(display_letters(indexes_guessed, word_chosen))
            print("The word has been uncovered! You win!")
            break

        if attempts <= 0:
            # Tell the user that they ran out of attempts.
            print("No attempts left. Game over.")
            # Then, unlock the word to show the user.
            unlock_all(indexes_guessed, word_chosen)
            print("The word is:")
            print(display_letters(indexes_guessed, word_chosen))
            break

        # Print the attempts remaining, alongside the word in question
        print(f"Attempts Remaining: {str(attempts)}")
        print(display_letters(indexes_guessed, word_chosen))
        # Tell the user to guess a letter, then lowercase it.
        # If the user typed in a word, only select the first letter.
        guess = input("Guess a letter: ")
        final_guess = guess.lower()[0]

        # Check if we already have the letter guessed.
        if check_guess_letter_exists(indexes_guessed, final_guess, word_chosen):
            print("You already guessed that letter.")
            continue

        # If our choice is wrong, decrease the attempts.
        if not process_guess(indexes_guessed, final_guess, word_chosen):
            print("Wrong choice. One attempt deducted.")
            attempts -= 1

game_main()
