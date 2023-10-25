mt = [0, 1, 4, 5, 7, 8]
# gesucht: [1, 3, 1, 2, 1]
differenzen = [ mt[x] - mt[x-1] for x in range(0, len(mt))] 
#differenzen = [ mt[x+1] - mt[x] for x in range(0, len(mt)-1)] 
print(differenzen)