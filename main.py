SPIELFELD_BREITE = 40
SPIELFELD_HOEHE = 25

SPIELER_X = 5
SPIELER_Y = 5

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
