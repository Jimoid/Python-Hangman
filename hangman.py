#!/usr/bin/env python
import random


game_word = ""
blanked_word = ""
player_guesses = []
no_wrong_guesses = 0

"""Simple terminal implementation of the classic Hangman game"""

def main():
    print("Welcome to\n")
    print("""
     _
    | |
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                       __/ |
                      |___/


    """)


def random_word():
    with open('/home/jimmy/Code/Python/Python-Hangman/dictionary_850_words.txt') as f:

        #variable to hold the dictionary of words used in the game
        dictionary_data = f.read().splitlines()
        #print (dictionary_data[:8])

        return random.choice(dictionary_data)



def check_guess(guess):
    #check if the guessed letter is in the hidden word
    if guess in game_word:

        #find out how many times the letter appears
        no_occurences = game_word.count(guess)
        if no_occurences == 1:
            print ("Your guess appears once in the word.")
        else:
            print ("Your guess appears " + str(no_occurences) + " times in the word.")

        #replace the underscore in the blanked word with the correctly guessed letter
        substring_idx = 0
        while no_occurences:
            print ("substring_idx = " + str(substring_idx))
            substring_idx = game_word.find(guess, substring_idx+1)
            print ("substring_idx = " + str(substring_idx))
            no_occurences -= 1
            print("Number of remaining occurences: " + str(no_occurences))

            blanked_word_list = list(blanked_word)
            blanked_word_list[(substring_idx*2)] = guess
            blanked_word = "".join(blanked_word_list)
            print (blanked_word)
        #while

    else:
        print("Unlucky, your guess was incorrect.")

        #enter a elif block to determine which animation to draw

        if no_wrong_guesses == 0:

            print("""







            =========
            """)

            no_wrong_guesses += 1

        elif no_wrong_guesses == 1:
            print("""

                  |
                  |
                  |
                  |
                  |
            =========
            """)

            no_wrong_guesses += 1

        elif no_wrong_guesses == 2:
            print("""
              +---+
                  |
                  |
                  |
                  |
                  |
            =========
            """)

            no_wrong_guesses += 1

        elif no_wrong_guesses == 3:

            print("""
              +---+
              |   |
                  |
                  |
                  |
                  |
            =========
            """)

            no_wrong_guesses += 1

        elif no_wrong_guesses == 4:

            print("""
              +---+
              |   |
              O   |
                  |
                  |
                  |
            =========
            """)

            no_wrong_guesses += 1

        elif no_wrong_guesses == 5:

            print("""
              +---+
              |   |
              O   |
              |   |
                  |
                  |
            =========
            """)

            no_wrong_guesses += 1

        elif no_wrong_guesses == 6:

            print("""
              +---+
              |   |
              O   |
             /|   |
                  |
                  |
            =========
            """)

            no_wrong_guesses += 1

        elif no_wrong_guesses == 7:

            print("""
              +---+
              |   |
              O   |
             /|\  |
                  |
                  |
            =========
            """)

            no_wrong_guesses += 1

        elif no_wrong_guesses == 8:

            print("""
              +---+
              |   |
              O   |
             /|\  |
             /    |
                  |
            =========
            """)

            no_wrong_guesses += 1

        elif no_wrong_guesses == 9:

            print("""
              +---+
              |   |
              O   |
             /|\  |
             / \  |
                  |
            =========
            """)

            no_wrong_guesses += 1





if __name__ == "__main__":

    main()
    game_word = random_word().lower()
    print(game_word)

    print("The word you must guess looks like this:")
    blanked_word = "_ " * len(game_word)
    print (blanked_word)

    guess = input ("Enter a letter to see if it is contained in the word: ")
    #guess = "e".lower()
    player_guesses.append(guess)

    check_guess(guess)

    print ("\nYour guesses are: " + str(player_guesses))
