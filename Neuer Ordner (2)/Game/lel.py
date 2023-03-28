revealed_letters={
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
    "k" : True,
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
    "z" : False
}
word = "kot"
for letter in word:
    if revealed_letters[letter] == False:
        print("_", end=" ")
    else:
        print(letter, end=" ")

