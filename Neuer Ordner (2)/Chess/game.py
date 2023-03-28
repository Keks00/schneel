import os
from display import chess_board
from legal import checklegal
from display import reset
from functions import user_input

def game_loop():
    slots = reset()
    game = True
    while game == True:
        move, pos, type = user_input(slots)
        legal, pos = checklegal(type,pos,move,slots)
        if legal == True:
            slots.update({f"{move}": "  "})
            slots.update({f"{pos}": type})
            chess_board(slots)
game_loop()