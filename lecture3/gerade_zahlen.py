# Lese k vom Benutzer,
# gebe alle geraden Zahlen im Bereich 1..k aus
k = int(input("K?"))
for i in range(1, k+1):
    if i % 2 == 0:
        print(i)