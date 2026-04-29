N = int(input())
P = []

for i in range(N):
    p = int(input())
    P.append(p)

_max = max(P)
ans = sum(P) - _max + _max // 2

print(ans)
