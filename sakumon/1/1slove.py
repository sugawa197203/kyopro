N, M = map(int, input().split())
S = input().lower()
T = input().lower()

charcount = dict()
for c in S:
    if c not in charcount:
        charcount[c] = 0
    charcount[c] += 1

for c in T:
    if c not in charcount:
        print("No")
        exit()
    charcount[c] -= 1
    if charcount[c] == -1:
        print("No")
        exit()
print("Yes")
