# Zeige ein Label für das aktuelle Passwort an
# Gebe einen Button für ein neues PW an

import tkinter 
import os 
haupt_fenster = tkinter.Tk()
#
from pw_logik import generiere_passwort
from pwgen import lese_woerter_aus_txt
# Pfad zum Verzeichnis, in dem das Skript ausgeführt wird
skript_verzeichnis = os.path.dirname(os.path.abspath(__file__))

# Der vollständige Pfad zur Dateiz
adjektive_pfad = os.path.join(skript_verzeichnis, "adjektive.txt")
nomen_pfad = os.path.join(skript_verzeichnis, "nomen.txt")

adjektive = lese_woerter_aus_txt(adjektive_pfad)
nomen = lese_woerter_aus_txt(nomen_pfad)

def ziehe_neues_pw():
    neues_passwort = generiere_passwort(nomen, adjektive)
    passwort_label.configure(text=neues_passwort)

button = tkinter.Button(haupt_fenster, text = "Generiere Passwort", command=ziehe_neues_pw)
button.grid(row=1, column=0)

passwort_label = tkinter.Label(haupt_fenster, text="")
passwort_label.grid(row=0, column=0)

haupt_fenster.mainloop()