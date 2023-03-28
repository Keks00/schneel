import random
import time
import sys
input_choice = 0
difficulty = 0
damage = 0
damage_mult = 1
critchance2 = 0
crit_tf : False
playername = input("NAME : ")
while difficulty != 1 and difficulty !=2 and difficulty !=3 and difficulty !=4 and difficulty !=5:
    difficulty = input("Difficulty (1-5) : ")
    try:
        difficulty = int(difficulty)
    except:
        ValueError
critchance = (int(difficulty)*10 - 50)*-1
critchance_enemy = int(difficulty)*10
hitchance = random.randint(60,100)
hitchance_enemy = random.randint(40,100)
hitchance_enemy2 = 0
hitchance2 = 0
hp_player = (int(difficulty)*7 - 80)*-1
dmg_player = 5
enemy_hp = int(difficulty)*12
dmg_enemy = 5
fight = True
while fight == True:
    critchance2 = random.randint(1, 100)
    if critchance >= critchance2:
        crit_tf = 2
    else:
        crit_tf = 1
    time.sleep(0.4)
    print("1.Attack")
    time.sleep(0.4)
    print("2.Defend")
    time.sleep(0.4)
    print("3.Heal")
    time.sleep(0.4)
    print("4.Give Up")
    time.sleep(0.5)
    while input_choice != "1" and input_choice != "2" and input_choice != "3" and input_choice != "4":
        input_choice = input("Choose the action (Number between 1-4) : ")
    if input_choice == "1":
        hitchance2 = random.randint(1,100)
        if hitchance >= hitchance2:
            enemy_hp -= (((random.randint(8,12) * int(dmg_player)) * int(crit_tf))/10)
            print("Hit! Your enemy has %d HP left" % enemy_hp)
        else:
            print("You missed! Your enemy has %d HP left" % enemy_hp)
        time.sleep(2)
    if input_choice == "2":
        damage_mult = (random.randint(2, 4)/5 )
        print("You will recieve a %f multiplier on the enemies next attack " % damage_mult)
        time.sleep(2)
    if input_choice == "3":
        healed = float(random.randint(4,25)/5)
        (hp_player) +=  healed
        print("You Healed %f HP" % healed)
        time.sleep(2)
    if input_choice == "4":
        sys.exit("You Left! Good Bye ;)")
    if enemy_hp <= 0:
        sys.exit("Enemy died!")
    input_choice = "0"
    print("Enemies turn : ")
    time.sleep(2)
    hitchance_enemy2 = random.randint(1,100)
    if hitchance_enemy >= hitchance_enemy2:
        critchance2 = random.randint(1, 100)
        if critchance_enemy >= critchance2:
            hp_player -= (random.randint(8,12) * int(dmg_enemy)/5)
        else:
            hp_player -= (random.randint(8,12) * int(dmg_enemy)/10)* float(damage_mult)
        print("Hit! You have %d HP left" % hp_player)
    else:
        print("Miss! You have %d HP left" % hp_player)
    time.sleep(3)
    damage_mult = 1
    if hp_player <= 0:
        sys.exit("You died!")
else:
        print("%s's turn : " % playername)
from functions import data_update
data_update(1)