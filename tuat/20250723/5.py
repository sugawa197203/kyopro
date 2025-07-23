from itertools import product
N = int(input())
A = []
for _ in range(N):
    _A = []
    a = int(input())
    for _ in range(a):
        x, y = map(int, input().split())
        _A.append((x, y))
    A.append(_A)

ans = 0
for i in product((True, False), repeat=N):
    count = i.count(True)
    if count < ans:
        continue
    if count == 0:
        continue
    f = False
    for AA in A:
        if f:
            break
        for (x, y) in AA:
            if i[x - 1] != (y == True):
                f = True
                break
    if f:
        continue
    ans = max(ans, count)

print(ans)

