import random
import string

def generiere_passwort(nomen : list, adjektive : list):
    gezogen_nomen = random.choice(nomen)
    gezogen_adjektiv = random.choice(adjektive)
    gezogene_zahl = random.randint(0, 100)

    gezogenes_sonderzeichen = random.choice(string.punctuation)
    passwort = gezogen_adjektiv + gezogen_nomen + str(gezogene_zahl) + gezogenes_sonderzeichen
    return passwort