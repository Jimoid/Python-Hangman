#!/usr/bin/env python
import sys
import os
import random

game_dictionary = 'dictionary_850_words.txt'
game_word = ""
game_word_letters = []
blanked_word = ""
player_guesses = []
number_wrong_guesses = 0

"""Simple terminal implementation of the classic Hangman game"""

def welcome():
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
    with open(os.path.join(sys.path[0], game_dictionary), "r") as f:

        #variable to hold the dictionary of words used in the game
        dictionary_data = f.read().splitlines()
        return random.choice(dictionary_data)



def check_status():

    # check the current player_guesses against the game_word_letters
    correct_guesses = 0

    for letter in game_word_letters:
        if letter in player_guesses:
            # check the number of correct letters against the number of
            # distinct letters in the game_word
            correct_guesses += 1
            if correct_guesses == len(game_word_letters):
                return "winner"
            else:
                continue
        elif letter not in player_guesses:
            return "next_guess"




def play():
    #print ("check_status = " + check_status())
    if check_status() == "next_guess" and number_wrong_guesses < 10:
        guess = input ("\nEnter a letter to see if it is contained in the word: ")
        player_guesses.append(guess)
        check_guess(guess)

        print (blanked_word)
        print ("\nYour guesses are: " + str(player_guesses))
        print ("You have " + str(9 - number_wrong_guesses) + " guesses remaining.\n\n\n")
        play()

    elif check_status() == "next_guess" and number_wrong_guesses == 10:

        print ("\nToo bad partner, you lost. Better luck next time :-)\n")
        print ("The word you were looking for was: " + game_word)
        exit()

    elif check_status() == "winner":

        print("""
                                            _         _       _   _
                                           | |       | |     | | (_)
             ___ ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___
            / __/ _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __|
           | (_| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \\
            \___\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/
                             __/ |
                            |___/

        Congrats, you beat me ;-P""")
        exit()




def check_guess(guess):


    global number_wrong_guesses
    global blanked_word

    #check if the guessed letter is in the hidden word
    if guess in game_word:

        #find out how many times the letter appears
        no_occurences = game_word.count(guess)
        if no_occurences == 1:
            print ("\nYour guess appears once in the word.\n")
        else:
            print ("\nYour guess appears " + str(no_occurences) + " times in the word.\n")

        #replace the underscore in the blanked word with the correctly guessed letter
        substring_idx = 0
        while no_occurences > 0:
            ###print ("substring_idx = " + str(substring_idx))

            if substring_idx == 0:
                #case when the guessed letter is the first occurence of the letter in the game_word
                substring_idx = game_word.find(guess, substring_idx)
            else:
                #case when the guessed letter is not the first occurence of the letter of the game_word
                substring_idx = game_word.find(guess, substring_idx+1)


            ###print ("substring_idx = " + str(substring_idx))
            no_occurences -= 1
            ###print("Number of remaining occurences: " + str(no_occurences))

            blanked_word_list = list(blanked_word)
            blanked_word_list[(substring_idx*2)] = guess
            blanked_word = "".join(blanked_word_list)
            #print (blanked_word)


    else:
        print("\nUnlucky, your guess was incorrect.")
        ###print (number_wrong_guesses)

        #enter a elif block to determine which animation to draw

        if number_wrong_guesses == 0:

            print("""







            =========
            """)

            number_wrong_guesses += 1

        elif number_wrong_guesses == 1:
            print("""

                  |
                  |
                  |
                  |
                  |
            =========
            """)

            number_wrong_guesses += 1

        elif number_wrong_guesses == 2:
            print("""
              +---+
                  |
                  |
                  |
                  |
                  |
            =========
            """)

            number_wrong_guesses += 1

        elif number_wrong_guesses == 3:

            print("""
              +---+
              |   |
                  |
                  |
                  |
                  |
            =========
            """)

            number_wrong_guesses += 1

        elif number_wrong_guesses == 4:

            print("""
              +---+
              |   |
              O   |
                  |
                  |
                  |
            =========
            """)

            number_wrong_guesses += 1

        elif number_wrong_guesses == 5:

            print("""
              +---+
              |   |
              O   |
              |   |
                  |
                  |
            =========
            """)

            number_wrong_guesses += 1

        elif number_wrong_guesses == 6:

            print("""
              +---+
              |   |
              O   |
             /|   |
                  |
                  |
            =========
            """)

            number_wrong_guesses += 1

        elif number_wrong_guesses == 7:

            print("""
              +---+
              |   |
              O   |
             /|\  |
                  |
                  |
            =========
            """)

            number_wrong_guesses += 1

        elif number_wrong_guesses == 8:

            print("""
              +---+
              |   |
              O   |
             /|\  |
             /    |
                  |
            =========
            """)

            number_wrong_guesses += 1

        elif number_wrong_guesses == 9:

            print("""
              +---+
              |   |
              O   |
             /|\  |
             / \  |
                  |
            =========
            """)

            number_wrong_guesses += 1





if __name__ == "__main__":

    # say hello
    welcome()

    # select a word for the game
    game_word = random_word().lower()



    # turn the game_word string into a list of individual characters
    # and add unique members to the game_word_letters list
    for letter in list(game_word):
        # check if letter exists in game_word_letters or not
        if letter not in game_word_letters:
            game_word_letters.append(letter)

    ###print (game_word)
    ###print (game_word_letters)

    # generate the blanked_word and display
    print("The word you must guess looks like this:\n")
    blanked_word = "_ " * len(game_word)
    print (blanked_word)



    # main function of the game
    # if set(player_guesses) < set(game_word_letters):
    play()
