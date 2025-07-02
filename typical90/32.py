from itertools import permutations

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
XY = set()
for _ in range(M):
    x, y = map(int, input().split())
    XY.add((x, y))
    XY.add((y, x))

ans = 10000000
for p in permutations(range(N)):
    _ans = 0
    for i in range(N-1):
        if (p[i]+1, p[i+1]+1) in XY:
            break
        _ans += A[p[i]][i]
    else:
        ans = min(ans, _ans + A[p[-1]][-1])

print(ans if ans != 10000000 else -1)


