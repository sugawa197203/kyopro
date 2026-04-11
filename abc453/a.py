N = int(input())
S = input()
f = True
for s in S:
    if f and s == "o":
        continue
    f = False
    print(s, end="")