from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

AA = [[0] * N for _ in range(11)]

Counts = [defaultdict(int) for _ in range(11)]
ans = 0

for i in range(N):
    a = A[i]
    for j in range(11):
        AA[j][i] = (a * (10 ** j)) % M 
        Counts[j][AA[j][i]] += 1


for i in range(N):
    a = A[i]
    length = len(str(a))
    count = Counts[length]
    mod = a % M
    _ans = count[(M - mod) % M]
    ans += _ans

print(ans)