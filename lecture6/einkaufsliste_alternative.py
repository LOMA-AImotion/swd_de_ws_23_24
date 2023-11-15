# Frage Benutzer solange nach Gegenständen zum Einkaufen bis er oder sie "Nein" 
# eingibt
# Solange ja:
#   Frage nach Bezeichnung
#   Frage nach Anzahl
# Gib am Schluss das ganze Dictionary aus und die keys() und values() 

nicht_stoppen = True
einkaufsliste = {}

while nicht_stoppen: 
    bezeichnung = input("Was möchtest du einkaufen?")
    anzahl = int(input("Wieviel davon?"))
    einkaufsliste[bezeichnung] = anzahl 

    weiter_einkaufen = input("Weiter einkaufen? (ja|nein)")
    if weiter_einkaufen == "nein":
        nicht_stoppen = False

print(einkaufsliste)
print(einkaufsliste.keys())
print(einkaufsliste.values())