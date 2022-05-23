# Projekt
Hier geht es um das Projekt ansich und wie wir das umsetzen können.


## Eingabe
In einem Schere-Stein-Papier Spiel, benötigt man irgendeine Art von Eingabe um den Benutzer es zu ermöglichen unterschiedliche Werte (Schere, Stein oder Papier) zu wählen. Dafür müssen wir uns überlegen wie wir es darstellen wollen. Wir haben uns dafür im Kurs geeinigt, ein Array zu nehmen damit wir nachher für den Computer leichter den Wert per Zufall ermitteln können. Dafür können wir zuerst ein Array erstellen und darin die vorhandenen Werte speichern.

```python3
auswahl = ["Schere", "Stein", "Papier"]
```

Danach brauchen wir ein Menü um dem Benutzer leichter und in verstädnlicher Art und Weise mitteilen zu können, welche Eingabe er tätigen kann. Um das Menü leichter an verschiedenen Stellen benutzen zu können, stellen wir das als Funktion dar.

```python3
def gebeSpielstandAus():
    print("Spielstand " + str(spielstand_links) + ":" + str(spielstand_rechts))
    print("1 =  Schere")
    print("2 =  Stein")
    print("3 =  Papier")
```

Innerhalb der Funkion, werden zwei Variablen benutzt um den Spielstand darzustellen. Dafür muss vor der Funktion folgendes stehen:

```python3
spielstand_links = 0
spielstand_rechts = 0
```

## Auswertung - den Sieger bestimmen

Um die Eingabe mit Worten zu beschreiben und damit umzugehen müssen wir noch die Nummern in die Werte aus unserem Array ziehen. 

Auch dafür definieren wir zwei Variablen. Eine für unsere Eingabe und eine für den Computer. Danach können wir mit der Eingegebenen Zahl auf das Array zu greifen. Das ganze können wir ebenfalls in einer extra Funktion machen, die uns den Sieger ermittelt. 

```python3
def bestimmeSieger(auswahl1, auswahl2):
    auswahl1_wort = auswahl[auswahl1]
    auswahl2_wort = auswahl[auswahl2]

# Aufgerufen wird die Funktion anschließend so:
sieger = bestimmeSieger(meine_auswahl, gegnerische_auswahl)
print(sieger)
```

Erweitert wird die Funktion nun mit der Logik, den Sieger zu ermitteln. Dafür brauchen wir einen Vergleich, der prüft ob die Werte gleich sind oder aber das Gewinnen oder Verlieren bestimmt.

### Unentschieden
Ein Unentschieden ist sehr einfach, da hier einfach geprüft werden muss ob zwei Werte gleich sind. Das kann wie folgt getan werden:

```python3
if auswahl1_wort == auswahl2_wort:
    return "Unentschieden"
```

### Gewonnen
Noch zu machen in der nächsten Woche

### Verloren
Noch zu machen in der nächsten Woche 


## Vollständige Code 

Der Vollständige Code sieht nun so:

```python3
spielstand_links = 0
spielstand_rechts = 0

def gebeSpielstandAus():
    print("Spielstand " + str(spielstand_links) + ":" + str(spielstand_rechts))
    print("1 =  Schere")
    print("2 =  Stein")
    print("3 =  Papier")


auswahl = ["Schere", "Stein", "Papier"]

meine_auswahl = 0
gegnerische_auswahl = 2


def bestimmeSieger(auswahl1, auswahl2):
    auswahl1_wort = auswahl[auswahl1]
    auswahl2_wort = auswahl[auswahl2]

    if auswahl1_wort == auswahl2_wort:
        return "Unentschieden"
    if auswahl1_wort == "Schere" and auswahl2_wort == "Papier":
        return "Gewonnen"
    if auswahl1_wort == "Papier" and auswahl2_wort == "Schere":
        return "Verloren"



sieger = bestimmeSieger(meine_auswahl, gegnerische_auswahl)
print(sieger)
```