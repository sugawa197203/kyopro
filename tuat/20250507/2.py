import math
N, D, P = map(int, input().split())
F = list(map(int, input().split()))

sumf = sum(F)
ans = sumf
F = sorted(F, reverse=True)

for dcnt in range(math.ceil(N / D) + 1):
    _F = sum(F[dcnt * D:dcnt * D + D])
    if P < _F:
        ans = ans - _F + P


print(ans)