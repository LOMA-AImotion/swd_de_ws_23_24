# Lese k vom Benutzer
# Baue eine Menge (Set) wie folgt:
# - für j zwischen 1 und k
# - füge z.B. (1, "x"), (2, "xx") ein
# Z.B. k = 3 -> {(1,"x"), (2, "xx"), (3, "xxx")}
#-----------------------------------------------
k = int(input("Welches k?"))

menge = { (i, i * "x") for i in range(1, k+1) }
print(menge)

# Alternative:
menge2 = set()
for i in range(1, k+1):
    menge2.add ( (i, i*"x") )
print(menge2)
        