# Frage Benutzer solange nach Gegenständen zum Einkaufen bis er oder sie "Nein" 
# eingibt
# Solange ja:
#   Frage nach Bezeichnung
#   Frage nach Anzahl
# Gib am Schluss das ganze Dictionary aus und die keys() und values() 

einkaufen = []
anzahl = []
nicht_stoppen = True

while nicht_stoppen: 
    einkaufen.append(input("Was möchtest du einkaufen?"))
    anzahl.append(int(input("Wieviel davon?")))
    weiter_einkaufen = input("Weiter einkaufen? (ja|nein)")
    if weiter_einkaufen == "nein":
        nicht_stoppen = False

einkaufsliste = dict(zip(einkaufen, anzahl))
print(einkaufsliste)
print(einkaufsliste.keys())
print(einkaufsliste.values())