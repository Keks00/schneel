def test_if_white(slots,move):
    sucess = False
    if slots[f"{move}"] in ["♜ ","♞ ","♝ ","♚ ","♛ ","♟ "]:
        return True
    return False

def turn_x_to_num(move,slots):
    x = (move[:1])
    sucess = False 
    try:
        y = int(move[1:])
    except:
        ValueError
        y = None
    if y in range(1,9):
        if x in ["a","b","c","d","e","f","g","h"]:
            if x == "a":
                x = 1 
            if x == "b":
                x = 2 
            if x == "c":
                x = 3 
            if x == "d":
                x = 4 
            if x == "e":
                x = 5 
            if x == "f":
                x = 6 
            if x == "g":
                x = 7 
            if x == "h":
                x = 8
            move = y*10+x
            sucess = True
    return(move, sucess)



def user_input(slots):
        sucess = False
        move_f = input("move from : ")
        move_f, sucess = turn_x_to_num(move_f,slots)
        if sucess == True:
            sucess = test_if_white(slots,move_f)
        while sucess == False:
            move_f = input("move from : ")
            move_f, sucess = turn_x_to_num(move_f,slots)
            if sucess == True:
                sucess = test_if_white(slots,move_f)

        sucess = False
        move_t = input("move to : ")
        move_t, sucess = turn_x_to_num(move_t,slots)
        while sucess == False:
            move_t = input("move to : ")
            move_t, sucess = turn_x_to_num(move_t,slots)
        type = slots["%s" % (move_f)]
        return(move_f,move_t, type)


def type_conversion(type):
    if type == "♟ ":
        type = "pawn"
    elif type == "♜ ":
        type = "rook"
    elif type == "♝ ":
        type = "bishop"
    elif type == "♞ ":
        type = "knight"
    elif type == "♛ ":
        type = "queen"
    elif type == "♚ ":
        type = "king"
    return type
