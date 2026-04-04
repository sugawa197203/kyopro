N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]
M = int(input())
S = [input() for _ in range(M)]

d = dict()

for s in S:
    l = len(s)
    for i, c in enumerate(s):
        if (i, c, l) not in d:
            d[(i, c, l)] = 0
        d[(i, c, l)] += 1

for j in range(M):
    _S = S[j]
    if len(_S) != N:
        print("No")
        continue
    f = True
    for i, c in enumerate(_S):
        if (AB[i][1] - 1, c, AB[i][0]) not in d:
            print("No")
            f = False
            break
        if d[(AB[i][1] - 1, c, AB[i][0])] == 0:
            print("No")
            f = False
            break
    
    if f:
        print("Yes")


