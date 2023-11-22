import webbrowser

#webbrowser.open("https://www.aimotion.de")

wuerfel_moeglichkeiten = ["*"*i for i in range(1, 7)]
# ziehe zufällig
from random import choice
gezogen = choice(wuerfel_moeglichkeiten)
print("Gezogen: ", gezogen)