N, M, K = map(int, input().split())
A = list(map(int, input().split()))
if N == M:
    print(*[0]*N)
    exit()
sumA = sum(A)
nokori = K - sumA
import bisect
print(nokori, sumA, K)
AA = [(a, i, -1) for i, a in enumerate(A)]
AA.sort(key=lambda x: x[0], reverse=True)
ruisekiAA = [0] * (N+1)
for i in range(N):
    ruisekiAA[i+1] = ruisekiAA[i] + AA[i][0]

print(AA)
print(A)

boader = AA[M]
boader2 = AA[M+1]
for i in range(N):
    _nokori = nokori
    ind = bisect.bisect_right(AA, AA[i][0] + _nokori, key=lambda x: x[0])
    if M <= ind:
        continue
    before = _nokori
    while True:
        _nokori = _nokori // 2
        ind = bisect.bisect_right(AA, AA[i][0] + _nokori, key=lambda x: x[0])
        if ind < M:
            before = _nokori
            continue
        before = _nokori
        _nokori *= 3
        continue

        


