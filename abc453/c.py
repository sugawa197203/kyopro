from itertools import product

N = int(input())
L = list(map(int, input().split()))
ans = 0
for P in product([-1, 1], repeat=N):
    count = 0
    pos = 0
    for l, p in zip(L, P):
        _pos = pos
        pos += l * p
        if (_pos < 0 and 0 <= pos) or (0 <= _pos and pos < 0):
            count += 1
    ans = max(ans, count)
print(ans)

