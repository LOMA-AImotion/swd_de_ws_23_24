def flaeche(breite, hoehe):
    print("Bin ich in der Funktion?")
    flaecheninhalt = breite*hoehe
    # Fehler: print(flaecheninhalt)
    return flaecheninhalt

print("Passiert etwas?")
flaeche_thi = flaeche(100, 150)
print("Was ist die Fläche?", flaeche_thi)