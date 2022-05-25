# Die Phase1 umsetzen
Um Phase 1 umzusetzen würde ich mir zwei Schleifen anlegen, die die X- und die Y Richtung abdecken. Dafür kann ich entweder eine For-Schleife oder eine While-Schleife nehmen um das wie gewünscht umzusetzen.
Es macht normalerweise kaum einen Unterschied welche Schleife ich nehme, wichtig dabei ist nur, dass ich bei beiden auf verschiedene Sachen achten muss.

## Beispiel 1 - FOR-Schleife
Zuerst lege ich mir zwei verschiedene Variablen an, die einmal für die Spielfeld Breite und die Höhe stehen.

```python3
SPIELFELD_BREITE = 40
SPIELFELD_HOEHE = 25
```
> definition der beiden Variablen. Die Werte können natürlich auch andere sein.


Jetzt muss ich mit der for-Schleife von 0 bis zu der Spielfeld höhe gehen und danach nochmal mit einer weiteren Schleife den Wert bis zur Spielfeld Breite.
> Ich muss zuerst den Y-Wert bzw. die Y Richtung machen, da in der Konsole leider kein Rückweg eingebaut ist. Für uns heißt das, dass ich immer eine komplette Zeile mache und anschließend eine Zeile weiter springe. Die Reihenfolge wäre damit wie folgt: Zeichnen der kompletten Zeile und anschließend ein Weiter springen in die nächste und das gleiche nochmal tun. Da ich damit im inneren immer die Zeile machen, die hier Stellvertretend für X steht ist bei unseren zwei Schleifen auch X die innere Schleife.

```python3
for y in range(SPIELFELD_HOEHE):
    for x in range(SPIELFELD_BREITE):
        print("_", end="")
    print()
```

Das `in range` in Python ist eine eingebaute Funktion von Python, die mir die Möglichkeit gibt von einer Zahl bis zu einer anderen Zahl zu laufen innerhalb meiner Schleife. Da ich nur einen Parameter habe (meine Breite bzw. meine Höhe) läuft diese Funktion immer von 0 bis zu dem Wert. Alternativ kann ich auch den Startwert als erstes mitgeben und mit der zweiten Zahl den Endwert.

In der Python Funktion print ist Standardmäßig ein NewLine drin (das heißt nach jedem Print-Statement geht Python in eine neue Zeile. Das kann ich unterbinden, indem ich Python das Zeichen für das Ende mitgebe und zum Beispiel auf ein leeren Text ändere)

## Beispiel 2 - WHILE-Schleife

Die WHILE-Schleife hat erstmal einen ähnlichen Aufbau wie die FOR-Schleife, nur das wir uns hier auch um die Variablen kümmern müssen, die wir benötigen um zu Zählen und den richtigen Punkt zu haben.
Dafür kann ich mir vorher die zwei Variablen x und y erstellen und mit 0 belegen.

```python3
x = 0
y = 0
```

Anschließend kann ich meinen Aufbau genauso halten wie bei der FOR-Schleife, nur das ich am Anfang der ersten Scvhleife meinen X-Wert wieder auf 0 setzen muss, da diese Variable außerhalb der Schleife definiert wurde und damit überall auch gültigkeit hat und ihren Wert somit nicht verliert.

```python3
while(y < SPIELFELD_HOEHE):
    x = 0
    while(x < SPIELFELD_BREITE):
        x = x + 1
        print("_", end="")
    print()
    y = y + 1
```

