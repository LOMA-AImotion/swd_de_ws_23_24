def grundstueck_preis(breite, hoehe, preis=1, brutto=False):
    netto_preis = breite*hoehe*preis
    if brutto:
        return 1.19 * netto_preis
    else:
        return netto_preis

print(grundstueck_preis(5, 10))
print(grundstueck_preis(5, 10, 2))
print(grundstueck_preis(5, 10, preis=10))
print(grundstueck_preis(5, 10, brutto=True))