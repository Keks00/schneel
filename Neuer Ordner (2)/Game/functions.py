import json 
import random
import os
import time
from math import pi
from math import cos

### Reading and writing to the player database
def data_update(player_data):
    data = {}
    file_path = "player/saved/id_%i_data.json" % (player_data['id'])
    with open(file_path, 'r') as f:
        data = json.load(f)

    with open(file_path, 'w') as f:
        json.dump(data,f)


### aim function for weapons requiring aiming


def aim():
    hit = 0
    tries = 3
    tries_max = tries
    won = False
    num = random.randint(1,100)

#   Gameloop

    while won == False and tries != 0:
        guess = ""
        while guess not in range(1,101):
            guess = input("\n\tthe closer the better: ")
            if guess.isnumeric():
                guess = int(guess)
        os.system("cls")
        print("\t..AIMING..")
        print("\ttry and hit the number")
        print("\t%i/%i" % (tries-1,tries_max))
        if guess > num:#guess is higher than num
            print("       Too high!")
        elif guess < num: #guess is lower than num
            print("       Too low!")
        else:#if guess correct
            print("\n          HEADSHOT!\n")
            won = True
            hit = 1
        near_low = num - 10
        near_high = num + 10
        if guess in range(near_low, near_high) and guess != num:
            print("\n       Getting Closer")
        tries -= 1

#   damage calculation with the use of cosine

    mult = (2*(abs(cos((((num - guess))/50)*pi)))+hit)

    print(mult)
aim()

def shop(money,inventory,items,inflation):
    print("\tS H O P")

def sell_shop(inventory,items):
    sell_shop(inventory)
def buy_item(money):
    buy_item(money)
def show_inv(inventory,items):
    show_inv()
def map_selection(level):
    map_selection(level)



def sin_test():
    for i in range(0,100,1):
        print(cos(i/100), end=" ")
        print(i/100)
        time.sleep(0.5)
