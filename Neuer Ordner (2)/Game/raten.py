import random
import sys 
tries = 0
int1 = 1
tries2= int(input("How many times do you want to try?: "))
to = int(input("To what range do you want to go?: "))
random = random.randint(1,(int(to)))
while tries <= (int(tries2)) :
    value = int(input("enter a number between 1 and %d: " % (int(to))))
    if value == random:
        sys.exit("You Won!")
        tries =+ int(tries2)
    elif int(tries) < int(tries2) - 1:
        tries += 1
        print("Welp! Try Again")
        if value > random:
            print("Too High!")
        else:
            print("Too Low!")
            print("Tries left: %d" % (int(tries2) - int(tries)))
    else:
        sys.exit("You Lost!")
        tries =+ tries2
