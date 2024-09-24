Q = int(input())

D = dict()
typecount = 0

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        d = D.get(q[1], 0)
        if d == 0:
            typecount += 1
        D[q[1]] = d + 1        
    elif q[0] == 2:
        d = D[q[1]]
        if d == 1:
            typecount -= 1
        D[q[1]] = d - 1
    else:
        print(typecount)