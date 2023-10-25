alle_plaetze = 10
reservierte_plaetze = 0

# solange noch Platz ist, nehme Anrufe entgegen
while reservierte_plaetze < alle_plaetze:
    name = input("Wer ruft an?")
    platzwunsch = int(input("Wie viele Plaetze?"))

    if (alle_plaetze - reservierte_plaetze) >= platzwunsch:
        reservierte_plaetze = reservierte_plaetze + platzwunsch
        print("OK, ist reserviert. ", 
              reservierte_plaetze , " / ", 
              alle_plaetze, "belegt")
    else: 
        print("Haben leider nicht genug Platz")
