#this is a quick write up of hangman with its most simple version


import random

def hangman():
    word_list = ["apple", "banana", "orange", "mango", "strawberry"]  # Add more words as desired
    word = random.choice(word_list).lower()
    guessed_letters = []
    tries = 6

    while True:
        hidden_word = ""
        for letter in word:
            if letter in guessed_letters:
                hidden_word += letter
            else:
                hidden_word += "_"

        print("Current word:", hidden_word)
        print("Guessed letters:", ", ".join(guessed_letters))
        print("Tries remaining:", tries)

        if hidden_word == word:
            print("Congratulations! You guessed the word correctly!")
            break

        if tries == 0:
            print("Oops! You ran out of tries. The word was:", word)
            break

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")

        elif guess.isalpha() and len(guess) == 1:
            guessed_letters.append(guess)

            if guess in word:
                print("Good guess!")

            else:
                print("Oops! That letter is not in the word.")
                tries -= 1

        else:
            print("Invalid input. Please enter a single letter.")

        print()

hangman()
