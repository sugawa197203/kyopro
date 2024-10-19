S = input()
now = S.index("A")
cost = 0
for a in "BCDEFGHIJKLMNOPQRSTUVWXYZ":
    cost += abs(now - S.index(a))
    now = S.index(a)

print(cost)