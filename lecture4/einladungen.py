kommando = input("Wen einladen? <niemand> zum Beenden")
gaeste_liste = []
while kommando != "niemand":
    gaeste_liste.append(kommando)
    kommando = input("Wen einladen? <niemand> zum Beenden")

print("Alle Gäste: ", gaeste_liste)