S = input()

Acount = 0
ABcount = 0
ABCcount = 0

for s in S:
    if s == 'A':
        Acount += 1
    elif s == 'B':
        if Acount > 0:
            ABcount += 1
            Acount -= 1
    elif s == 'C':
        if ABcount > 0:
            ABCcount += 1
            ABcount -= 1

print(ABCcount)
