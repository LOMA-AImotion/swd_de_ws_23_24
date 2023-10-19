# Berechne die Anzahl Jahre seitdem jemand wählen darf
name = input("Name?")
alter = int(input("Alter?"))
wahl_alter = 18

if alter > wahl_alter:
    diff = alter - wahl_alter
    print(name, "Du darfst seit", diff, "Jahren wählen.")
elif alter < wahl_alter:
    diff = wahl_alter - alter
    print(name, "Du musst noch", diff, "Jahre warten.")
else:
    print(name, "Du bist Erstwähler")