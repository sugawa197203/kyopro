from collections import Counter

S = input()

c = Counter(S)

west = c['W']
east = c['E']

print("East" if east > west else "West")
