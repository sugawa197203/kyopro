S = input()
T = input()

STdistance = 0
for i in range(len(S)):
    if S[i] != T[i]:
        STdistance += 1

print(STdistance)

for i in range(STdistance):
    buf = []
    for j in range(len(S)):
        if S[j] != T[j]:
            buf.append(S[:j] + T[j] + S[j+1:])
    
    buf.sort()
    S = buf[0]
    print(S)

