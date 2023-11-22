# Definiere die ReLU-Funktion
# Gib ihre Werte von -10 bis 10 aus
# relu(x) = 0, wenn x < 0
# relu(x) = x, wenn x >= 0
def relu(x : float) -> float:
    if x < 0:
        wert = 0
    else:
        wert = x
    return wert 
    

for x in range(-10, 11):    
    print(f"Wert für x = {x} ist {relu(x)}")
