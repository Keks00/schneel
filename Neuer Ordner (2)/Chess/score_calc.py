from display import reset



def calc_values(risks):
    point_map = {}
    for key,value in risks.items():
        try:
            if value[:1] == 2:
                point_map[key] == 10
        except: TypeError
    for key,value in risks.items():
        try:
            if value[:1] == 3:
                point_map[key] == 30
        except: TypeError
    for key,value in risks.items():
        try:
            if value[:1] == 4:
                point_map[key] == 30
        except: TypeError
    for key,value in risks.items():
        try:
            if value[:1] == 5:
                point_map[key] == 50
        except: TypeError
    for key,value in risks.items():
        try:
            if value[:1] == 6:
                point_map[key] == 90
        except: TypeError
    for key,value in risks.items():
        try:
            if value[:1] == 7:
                point_map[key] == 900
        except: TypeError
    print(risks)
    print(point_map)

# Checks for the fields the algorithm should avoid
def pawn_risks(risks,rewrite):
    rewrite_slot = rewrite
    try:
        if risks[rewrite_slot + -11] in range(0,10):
            risks[rewrite_slot + -11] += 10
        if risks[rewrite_slot + -9] in range(0,10):
            risks[rewrite_slot + -9] += 10  
    except:
         KeyError
    return risks


def knight_risk(risks,rewrite):
    out_of_range = [19,29,39,49,59,69,79,10,20,30,40,50,60,70,80]  
    rewrite_slot = rewrite

    try:
        if risks[rewrite_slot + -12] in range(0,10):
            risks[rewrite_slot + -12] += 10
        if risks[rewrite_slot + -21] in range(0,10):
            risks[rewrite_slot + -21] += 10
        if risks[rewrite_slot + -19] in range(0,10):
            risks[rewrite_slot + -19] += 10
        if risks[rewrite_slot + -8] in range(0,10):
            risks[rewrite_slot + -8] += 10
        if risks[rewrite_slot + 8] in range(0,10):
            risks[rewrite_slot + 8] += 10
        if risks[rewrite_slot + 19] in range(0,10):
            risks[rewrite_slot + 19] += 10
        if risks[rewrite_slot + 21] in range(0,10):
            risks[rewrite_slot + 21] += 10
        if risks[rewrite_slot + 12] in range(0,10):
            risks[rewrite_slot + 12] += 10
    except:
         KeyError
    return risks

def king_risk(risks,rewrite):
    rewrite_slot = rewrite
    try:
        if risks[rewrite_slot + -11] in range(0,10):
            risks[rewrite_slot + -11] += 10
        if risks[rewrite_slot + -10] in range(0,10):
            risks[rewrite_slot + -10] += 10
        if risks[rewrite_slot + -9] in range(0,10):
            risks[rewrite_slot + -9] += 10
        if risks[rewrite_slot + -1] in range(0,10):
            risks[rewrite_slot + -1] += 10
        if risks[rewrite_slot + 1] in range(0,10):
            risks[rewrite_slot + 1] += 10
        if risks[rewrite_slot + 9] in range(0,10):
            risks[rewrite_slot + 9] += 10
        if risks[rewrite_slot + 10] in range(0,10):
            risks[rewrite_slot + 10] += 10
        if risks[rewrite_slot + 11] in range(0,10):
            risks[rewrite_slot + 11] += 10
    except:
        KeyError
    return risks


def queen_risk(risks,rewrite):
    rewrite_slot = rewrite
    out_of_range = [19,29,39,49,59,69,79,10,20,30,40,50,60,70,80]  

    rewrite_slot += 11
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot += 11
    rewrite_slot = rewrite
    
    rewrite_slot -= 11
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break 
        rewrite_slot -= 11
    rewrite_slot = rewrite
    
    rewrite_slot += 9
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot += 9
    rewrite_slot = rewrite
    
    rewrite_slot -= 9
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot -= 9
    rewrite_slot = rewrite

    rewrite_slot += 1
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot += 1
    rewrite_slot = rewrite
    
    rewrite_slot -= 1
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot -= 1
    rewrite_slot = rewrite
    
    rewrite_slot += 10
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot += 10
    rewrite_slot = rewrite
    
    rewrite_slot -= 10
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot -= 10

    return risks

def bishop_risk(risks,rewrite):
    rewrite_slot = rewrite
    out_of_range = [19,29,39,49,59,69,79,10,20,30,40,50,60,70,80]  

    rewrite_slot += 11
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot += 11
    rewrite_slot = rewrite
    
    rewrite_slot -= 11
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot -= 11
    rewrite_slot = rewrite
    
    rewrite_slot += 9
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot += 9
    rewrite_slot = rewrite
    
    rewrite_slot -= 9
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot -= 9
    return risks


def rook_risk(risks,rewrite):
    rewrite_slot = rewrite
    out_of_range = [19,29,39,49,59,69,79,10,20,30,40,50,60,70,80]  


    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot += 1
    rewrite_slot = rewrite
    
    
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot -= 1
    rewrite_slot = rewrite
    
    
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot += 10
    rewrite_slot = rewrite
    
    
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot -= 10
    return risks

 
def figure_points():
    type_points = {}
    type_points["pawn"] = 10
    type_points["knight"] = 30
    type_points["bishop"] = 30
    type_points["rook"] = 50
    type_points["queen"] = 90
    type_points["king"] = 900
    return type_points
def coordinates_to_num(test_slots):
    
    score_pos = {
        "pawn":
        [ 0,  0,  0,  0,  0,  0,  0,  0,
         50, 50, 50, 50, 50, 50, 50, 50,
         10, 10, 20, 30, 30, 20, 10, 10,
          5,  5, 10, 25, 25, 10,  5,  5,
          0,  0,  0, 20, 20,  0,  0,  0,
          5, -5,-10,  0,  0,-10, -5,  5,
          5, 10, 10,-20,-20, 10, 10,  5,
          0,  0,  0,  0,  0,  0,  0,  0  ],
        "knight":
        [-50,-40,-30,-30,-30,-30,-40,-50,
         -40,-20,  0,  0,  0,  0,-20,-40,
         -30,  0, 10, 15, 15, 10,  0,-30,
         -30,  5, 15, 20, 20, 15,  5,-30,
         -30,  0, 15, 20, 20, 15,  0,-30,
         -30,  5, 10, 15, 15, 10,  5,-30,
         -40,-20,  0,  5,  5,  0,-20,-40,
         -50,-40,-30,-30,-30,-30,-40,-50],
        "bishop":
        [-20,-10,-10,-10,-10,-10,-10,-20,
         -10,  0,  0,  0,  0,  0,  0,-10,
         -10,  0,  5, 10, 10,  5,  0,-10,
         -10,  5,  5, 10, 10,  5,  5,-10,
         -10,  0, 10, 10, 10, 10,  0,-10,
         -10, 10, 10, 10, 10, 10, 10,-10,
         -10,  5,  0,  0,  0,  0,  5,-10,
         -20,-10,-10,-10,-10,-10,-10,-20],
        "rook": 
        [  0,  0,  0,  0,  0,  0,  0,  0,
           5, 10, 10, 10, 10, 10, 10,  5,
          -5,  0,  0,  0,  0,  0,  0, -5,
          -5,  0,  0,  0,  0,  0,  0, -5,
          -5,  0,  0,  0,  0,  0,  0, -5,
          -5,  0,  0,  0,  0,  0,  0, -5,
          -5,  0,  0,  0,  0,  0,  0, -5,
           0,  0,  0,  5,  5,  0,  0,  0],
        "queen":
        [-20,-10,-10, -5, -5,-10,-10,-20,
         -10,  0,  0,  0,  0,  0,  0,-10,
         -10,  0,  5,  5,  5,  5,  0,-10,
          -5,  0,  5,  5,  5,  5,  0, -5,
           0,  0,  5,  5,  5,  5,  0, -5,
         -10,  5,  5,  5,  5,  5,  0,-10,
         -10,  0,  5,  0,  0,  0,  0,-10,
         -20,-10,-10, -5, -5,-10,-10,-20],
        "king_early":
        [-30,-40,-40,-50,-50,-40,-40,-30,
         -30,-40,-40,-50,-50,-40,-40,-30,
         -30,-40,-40,-50,-50,-40,-40,-30,
         -30,-40,-40,-50,-50,-40,-40,-30,
         -20,-30,-30,-40,-40,-30,-30,-20,
         -10,-20,-20,-20,-20,-20,-20,-10,
          20, 20,  0,  0,  0,  0, 20, 20,
          20, 30, 10,  0,  0, 10, 30, 20],
        "king_late":
        [-50,-40,-30,-20,-20,-30,-40,-50,
         -30,-20,-10,  0,  0,-10,-20,-30,
         -30,-10, 20, 30, 30, 20,-10,-30,
         -30,-10, 30, 40, 40, 30,-10,-30,
         -30,-10, 30, 40, 40, 30,-10,-30,
         -30,-10, 20, 30, 30, 20,-10,-30,
         -30,-30,  0,  0,  0,  0,-30,-30,
         -50,-30,-30,-30,-30,-30,-30,-50]
    }



def if_risk(slots,move):
    risks = {}
    test_slot = 11
    while test_slot <= 88:
        print("! ",test_slot)
        if slots[f"{test_slot}"] == "  ":
           risks[test_slot] = 0
        elif slots[f"{test_slot}"] == "♖ ":
            risks[test_slot] = 3
        elif slots[f"{test_slot}"] == "♘ ":
            risks[test_slot] = 4
        elif slots[f"{test_slot}"] == "♗ ":
            risks[test_slot] = 5
        elif slots[f"{test_slot}"] == "♔ ":
            risks[test_slot] = 6
        elif slots[f"{test_slot}"] == "♕ ":
            risks[test_slot] = 7
        elif slots[f"{test_slot}"] == "♙ ":#["♖ ","♘ ","♗ ","♕ ","♔ ","♙ "]
            risks[test_slot] = 2            #["♜ ","♞ ","♝ ","♚ ","♛ ","♟ "]
        elif slots[f"{test_slot}"] == "♜ ":
            risks[test_slot] = -3
        elif slots[f"{test_slot}"] == "♞ ":
            risks[test_slot] = -4
        elif slots[f"{test_slot}"] == "♝ ":
            risks[test_slot] = -5
        elif slots[f"{test_slot}"] == "♚ ":
            risks[test_slot] = -6
        elif slots[f"{test_slot}"] == "♛ ":
            risks[test_slot] = -7
        elif slots[f"{test_slot}"] == "♟ ":#["♖ ","♘ ","♗ ","♕ ","♔ ","♙ "]
            risks[test_slot] = -2      

        if test_slot in range(18,88,10):
            test_slot += 3
            print(test_slot)
        else:
            test_slot += 1
    test_slot = 11
    while test_slot <= 88:
        rewrite_slot = test_slot


        match risks[test_slot]:
            case 3:
                 risks = rook_risk(risks,rewrite_slot)
            case 4:
                 risks = knight_risk(risks,rewrite_slot)
            case 5:
                 risks = bishop_risk(risks,rewrite_slot)
            case 6:
                 risks = queen_risk(risks,rewrite_slot)
            case 7:
                 risks = king_risk(risks,rewrite_slot)
            case 2:
                 risks = pawn_risks(risks,rewrite_slot)

        if test_slot in range(18,88,10):
            test_slot += 3
            print("2. ",test_slot)
        else:
            test_slot += 1
            print("!  2. ",test_slot)
    calc_values(risks)
    print("stop")
    return risks
slots = reset()
move = 41  
risks = if_risk(slots,move)
calc_values(risks)