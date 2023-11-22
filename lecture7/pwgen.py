def lese_woerter_aus_txt(file_name: str) -> list:
    """
    Liest Wörter aus einer Textdatei, wobei jedes Wort in einer eigenen Zeile steht.

    Parameters:
    - file_name (str): Der Dateipfad zur Textdatei.

    Returns:
    - list: Eine Liste von Wörtern aus der Datei.
    """
    try:
        with open(file_name, 'r') as file:
            # Lese alle Zeilen aus der Datei und entferne Leerzeichen und Zeilenumbrüche
            woerter = [line.strip() for line in file.readlines()]

        return woerter
    except FileNotFoundError:
        print(f"Die Datei '{file_name}' wurde nicht gefunden.")
        return []

# Pfad zu Adjektive und Nomen muss relativ zum Skript gesetzt werden
import os

# Pfad zum Verzeichnis, in dem das Skript ausgeführt wird
skript_verzeichnis = os.path.dirname(os.path.abspath(__file__))

# Der vollständige Pfad zur Datei
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
