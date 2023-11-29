def verdopple(x):
    return 2*x

def verdreifache(x):
    return 3*x

if input("Verdoppeln? (j|n)") == "j":
    meine_funktion = verdopple
else:
    meine_funktion = verdreifache

print(meine_funktion(10))