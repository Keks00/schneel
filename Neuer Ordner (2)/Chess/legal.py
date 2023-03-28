import os
from functions import type_conversion

def checklegal(type_symbol,move,pos,slots):
    type = type_conversion(type_symbol)
    legal = False

    #defines x and y for the position the move and the relative coordinate change
    px = int(str(pos)[1:])
    py = int(str(pos)[:1])
    mx = int(str(move)[1:])
    my = int(str(move)[:1])
    relx = mx - px
    rely = my - py

    #check for type
    if type == "rook":
        legal, move = check_rook(px,py,relx,rely,legal,pos,move,slots)
    elif type == "pawn":
        legal = check_pawn(px,py,relx,rely,legal,slots,move,pos)
    elif type == "bishop":
        legal, move = check_bishop(px,py,relx,rely,legal,pos,move,slots)
    elif type == "knight":
        legal = check_knight(px,py,relx,rely,legal,move)
    elif type == "queen":
        legal, move = check_queen(px,py,relx,rely,legal,pos,slots,move)
    elif type == "king":
        legal = check_king(px,py,relx,rely,legal)
    if legal == True:
        os.system("cls")
    return legal, move


#check if the pos change from the pawn is legal
def check_pawn(px,py,relx,rely,legal,slots, move, pos):
    if rely == 1 and relx == 0 and slots[f"{move}"] == "  ":
        legal = checkboard(px,py,relx,rely,legal)

    elif rely == 1 and abs(rely) == abs(relx) and slots[f"{move}"] in ["♖ "",♘ ""♗ ","♕ ","♔ ","♙ "]:
        legal = checkboard(px,py,relx,rely,legal)
    elif pos in range(21,29) and rely == 2 and relx == 0:
        legal = checkboard(px,py,relx,rely,legal)
    return legal

#check if the pos change from the rook is legal
def check_rook(px,py,relx,rely,legal,pos,move,slots):
    if relx in range(-8,8) and rely == 0 or rely in range(-8,8) and relx == 0:
        legal = checkboard(px,py,relx,rely,legal)
        if legal == True:
            move = rook_path(relx,rely,pos,move,slots)
    return legal, move

#check if the pos change from the bishop is legal 
def check_bishop(px,py,relx,rely,legal,pos,move,slots):
    if relx in range(-8,8) and abs(rely) == abs(relx):
        legal = checkboard(px,py,relx,rely,legal)
        if legal == True:
            move = bishop_path(relx,rely,pos,move,slots)
    return legal, move

#check if the pos change from the knight is legal
def check_knight(px,py,relx,rely,legal):
    if relx in[-1,1] and rely in [-2,2] or relx in [-2,2] and rely in [-1,1]:
     legal = checkboard(px,py,relx,rely,legal)
    return legal

#check if the pos change from the queen is legal
def check_queen(px,py,relx,rely,legal,pos,slots,move):
    if relx in range(-8,8) and abs(rely) == abs(relx) or rely in range(-8,8) and relx == 0:
        legal = checkboard(px,py,relx,rely,legal)
        if legal == True:
            move = queen_path(relx,rely,pos,move,slots)
    return legal, move

#check if the pos change from the king is legal
def check_king(px,py,relx,rely,legal):
    if relx in [-1,0,1] and rely in [-1,1]:
        legal = checkboard(px,py,relx,rely,legal)
    return legal


#check if the move is on the board
def checkboard(px,py,relx,rely,legal):
    if (px + relx) in range(1,9):
        if (py + rely) in range(1,9):
            return True 
        

def queen_path(relx,rely,pos,move,slots):
    if relx and rely > 0:
         move = bishop_path(relx,rely,pos,move,slots)
    else:
        move = rook_path(relx,rely,pos,move,slots)
    return move


def rook_path(relx,rely,pos,move,slots):
    check_field = pos
    while check_field != move:
        check_field_2 = check_field
        if relx > 0:
            check_field += 1
        elif relx < 0:
            check_field -= 1
        elif rely > 0:
            check_field += 10
        elif rely < 0:
            check_field -= 10
        if slots[f"{check_field}"] in ["♜ ","♞ ","♝ ","♚ ","♛ ","♟ "]:
            return check_field_2
        elif slots[f"{check_field}"] in ["♖ ","♘ ","♗ ","♕ ","♔ ","♙ "]:
            break 
    return check_field

def bishop_path(relx,rely,pos,move,slots):
    check_field = pos
    while check_field != move:
        check_field_2 = check_field    
        if relx > 0 and rely > 0:
            check_field += 11
        elif relx < 0 and rely > 0:
            check_field += 9
        elif relx > 0 and rely < 0:
            check_field += -9
        elif relx < 0 and rely < 0:
            check_field += -11
        if slots[f"{check_field}"] in ["♜ ","♞ ","♝ ","♚ ","♛ ","♟ "]:
            return check_field_2
        elif slots[f"{check_field}"] in ["♖ ","♘ ","♗ ","♕ ","♔ ","♙ "]:
            break 
    return check_field
    