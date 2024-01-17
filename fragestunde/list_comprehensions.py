bestellungen = [(2, "Schrauben", 3.95), (3, "Muttern", 1.50), (1, "Standleiter", 10.95)]
#einzelpreise = [bestellung[0] * bestellung[2] for bestellung in bestellungen]
einzelpreise = [anzahl * einzelpreis for anzahl, artikel, einzelpreis in bestellungen] 
print(einzelpreise)

sternchen = [ "*" * i for i in range(0, 10)]
print(sternchen)

sternchen_menge = { "*" * i for i in range(0, 10)}
print(sternchen_menge)

sternchen_dict = { i : "*" * i for i in range(0, 10)}
print(sternchen_dict)