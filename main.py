SPIELFELD_BREITE = 40
SPIELFELD_HOEHE = 25

PLAYER_X = 5  # P
PLAYER_Y = 5
SNAKE_X = 10  # S
SNAKE_Y = 10
DOOR_X = 15  # D
DOOR_Y = 15
KEY_X = 20  # K
KEY_Y = 20

for y in range(SPIELFELD_HOEHE):
    for x in range(SPIELFELD_BREITE):
        print("_", end="")
    print()

x = 0
y = 0

while(y < SPIELFELD_HOEHE):
    x = 0
    while(x < SPIELFELD_BREITE):
        x = x + 1
        print("_", end="")
    print()
    y = y + 1
