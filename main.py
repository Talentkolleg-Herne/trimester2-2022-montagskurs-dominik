from random import randint

SPIELFELD_BREITE = 50
SPIELFELD_HOEHE = 20


playerX = randint(1, SPIELFELD_BREITE)
playerY = randint(1, SPIELFELD_HOEHE)
SNAKE_X = randint(1, SPIELFELD_BREITE)
SNAKE_Y = randint(1, SPIELFELD_HOEHE)
DOOR_X = randint(1, SPIELFELD_BREITE)
DOOR_Y = randint(1, SPIELFELD_HOEHE)
KEY_X = randint(1, SPIELFELD_BREITE)
KEY_Y = randint(1, SPIELFELD_HOEHE)

LOSE = False


def movePlayer():
    global playerX, playerY

    inp = input("Bewege den Spieler mit w/a/s/d: ")

    if(inp == "w"):
        playerY = playerY - 1
    elif (inp == "s"):
        playerY = playerY + 1
    elif (inp == "a"):
        playerX = playerX - 1
    elif (inp == "d"):
        playerX = playerX + 1


while(not LOSE):
    for y in range(SPIELFELD_HOEHE):
        for x in range(SPIELFELD_BREITE):
            if playerX == (x+1) and playerY == (y+1):
                print("P", end="")
            elif SNAKE_X == (x+1) and SNAKE_Y == (y+1):
                print("S", end="")
            elif DOOR_X == (x+1) and DOOR_Y == (y+1):
                print("D", end="")
            elif KEY_X == (x+1) and KEY_Y == (y+1):
                print("K", end="")
            else:
                print("_", end="")
        print()

    # bewege spieler
    movePlayer()
    # bewege die schlange


# # Zukünftige Ideen
# * Schwierigkeitsgrade
# * Unterschiedliche Level (ggf. unterschiedliche Schlangentypen oder aber unterschiedliche Level formate)
# * leben vergeben
# * items erstellen (leben geben, schlange wegbewegen usw.)
