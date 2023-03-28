import random
gameloop = True
username = str(input("Bitte gib einen Spielernamen ein: "))

#Zahlenraten-Spiel
def zahlenRaten(name):
    print("Hallo %s. Los geht's mit Zahlenraten!" % (name))
    ##Randomzahl, die es zu erraten gilt
    ratezahl = random.randint(1, 100)

    ##Gameloop -> Boolean: True oder False
    aktiv = True
    #Anzahl der Versuche
    versuche = 0
    #Schleife, die immer wieder prüft, ob aktiv True oder False
    while aktiv:
        zahl = int(input("Zahl bitte:"))
        versuche = versuche + 1
        if ratezahl == zahl:
            print("Great! You won by guessing the number: %d" % (ratezahl))
            aktiv = False
        elif ratezahl > zahl:
            print("Die gesuchte Zahl ist größer...")
        elif ratezahl < zahl:
            print("Die gesuchte Zahl ist kleiner...") 
        if versuche < 8:
            print("Wrong. Try again...")
        else: 
            aktiv = False
            print("Game Over!")

#Hangman-Spiel
def hangman(name):
    aktiv = True
    life = 3
    letters_used = ""
    word_to_guess = "computerscience"

    print("Hallo %s. Willkommen zu Hangman!" % (name))
    while aktiv and life > 0: 
        fortschritt = ""
        #Anzeige des Wortes mit Unterstrichen
        #
 
        user_guess = str(input("Guess a letter -> ")).lower()
        if user_guess in letters_used:
            #Fall, dass der Buchstabe bereits verwendet wurde
            print("Buchstabe bereits verwendet, du Depp. Leben verloren")
            life -= 1
            print("Du hast noch %d Leben" % (life))

        elif user_guess in word_to_guess:
            user_guess = user_guess + ", "
            letters_used = letters_used + user_guess
            print("Bereits verwendet: %s" % (letters_used))
            #Fall, dass der Buchstabe mind. 1 mal im Wort vorkommt
            #Hinzufügen des Buchstaben zu "letters_used"
            print("Your guess was RIGHT!")
        
        elif user_guess not in word_to_guess:
            print("Better luck next time. Leben verloren")
            life -= 1
            print("Du hast noch %d Leben" % (life))
            user_guess = user_guess + ", "
            letters_used = letters_used + user_guess
    print("du hast keine leben mehr %s" % (name))


while gameloop:
    ##Hier soll man zwischen den Minigames wählen können
    print("Willkommen im Minigame-Menü.")
    print("Bitte Zahl eingeben, um das Minigame zu wählen:")
    print("1) ZAHLENRATEN")
    print("2) HANGMAN")
    print("0) EXIT")
    choice = int(input("Wahl: "))
    ###Wird 1 eingeben -> zahlenRaten
    ###Wird 2 eingeben -> hangman
    if choice == 1:
        zahlenRaten(username)
    elif choice == 2:
        hangman(username)
    elif choice == 0:
        exit()
    else: 
        print("Das Spiel gibt es noch nicht. Bitte wähle zwischen 1 und 2.")
    
hangman