# Pfad zu Adjektive und Nomen muss relativ zum Skript gesetzt werden
import os
from pwgen import lese_woerter_aus_txt

# Pfad zum Verzeichnis, in dem das Skript ausgeführt wird
skript_verzeichnis = os.path.dirname(os.path.abspath(__file__))

# Der vollständige Pfad zur Dateiz
adjektive_pfad = os.path.join(skript_verzeichnis, "adjektive.txt")
nomen_pfad = os.path.join(skript_verzeichnis, "nomen.txt")

adjektive = lese_woerter_aus_txt(adjektive_pfad)
nomen = lese_woerter_aus_txt(nomen_pfad)

fortsetzen = True
from pw_logik import generiere_passwort

while fortsetzen :
    print("Generiere Passwort ...")
    passwort = generiere_passwort(adjektive, nomen)
    print(passwort)
    fortsetzen = input("Fortsetzen? (j|n)") == "j"
