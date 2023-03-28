from multiprocessing.sharedctypes import Value
import sys
import os
import time

import logging
import random
def hangman():
    hangman_sprites = {
     10 :
     '''
     


    ''',
    9 :
    '''

    
    
        ===''',
    8 :
    '''
         |
         |
         |
        ===''',
    7 :
    '''
     +---+
         |
         |
         |
        ===''',
    6 :
    '''
     +---+
        \|
         |
         |
        ===''',
    5 :'''
     +---+
     O  \|
         |
         |
        ===''',
    4 :'''
     +---+
     O  \|
     |   |
         |
        ===''',
    3 :'''
     +---+
     O  \|
    /|   |
         |
        ===''',
    2 :'''
     +---+
     O  \|
    /|\  |
         |
        ===''',
    1 :
    '''
     +---+
     O  \|
    /|\  |
    /    |
        ===''',
    0:
    '''
     +---+
     O  \|
    /|\  |
    / \  |
        ===
  !!DEAD!!'''
    }
    revealedletters={
    "a" : False,
    "b" : False,
    "c" : False,
    "d" : False,
    "e" : False,
    "f" : False,
    "g" : False,
    "h" : False,
    "i" : False,
    "j" : False,
    "k" : False,
    "l" : False,
    "m" : False,
    "n" : False,
    "o" : False,
    "p" : False,
    "q" : False,
    "r" : False,
    "s" : False,
    "t" : False,
    "u" : False,
    "v" : False,
    "w" : False,
    "x" : False,
    "y" : False,
    "z" : False,
    "" : None
    }


    language = ""
    lang = {"de","en"}
    print("  H A N G M A N \n")
    while not language in lang:
        language = input("    (de/en): ")
    reset = ""

    if language == "de":
        filepath = "germanwords.txt"
        to = 189591
    else:
        filepath = "englishwords.txt"
        to = 2999
    with open(filepath) as f:
        for i in range(random.randint(1,to)):
            word = f.readline()

    word = word.strip("\n")

    tries = 10
    length = len(word)


    while tries > 0:
        letter = ""
        for key,value in revealedletters.items():
            if value == True:
                print("%s, " % (key), end="")

        while len(letter) != 1 or not letter in "abcdefghijklmnopqrstuvwxyz" or revealedletters[letter] == True:
            if len(letter) == 1 and letter in "abcdefghijklmnopqresuvwxyz"and revealedletters[letter] == True:
                print("You already tried that letter\n")
            print("\n    %i/10" % tries)
            letter = input(str("    letter: "))
        os.system("cls'''  '''")
        print("\n   .H A N G M A N.")
        revealedletters[letter] = True
        if letter in word:
                
                print("\n      Correct!\n")
        else:
            tries -= 1
            if tries != 1:
                print("\nYou were wrong. %s tries remaining\n" % tries)
            else:
                print("\nYou were wrong. %s try remaining\n" % tries)


        won = True
        for letter in word:
            if revealedletters[letter] == False:
                print("_ ", end=" ")
                won = False
            else:
                print(letter, end=" ")


        print("\n",hangman_sprites[tries])
        if won == True:
                    print("\n     You win.\n\n      %s\n" % word)
                    while reset != "y" and reset != "n":
                        reset = input(str("    Play again? (y|n): "))
                    if reset == "y":
                        import code_1
                        code_1
                    else:
                        sys.exit("  exit")


    else:
        print("    The word was %s\n" % word)
        print("    You lost.\n")
    while reset != "y" and reset != "n":
        reset = input(str("    Play again? (y|n): "))
    if reset == "y":
        hangman
    else:
        sys.exit("  exit")


hangman()