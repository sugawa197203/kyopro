from collections import Counter
from math import comb

N = int(input())
A = list(map(int, input().split()))

counter = Counter(A)
ans = 0

for v in counter.values():
    if v == 1:
        continue

    count = comb(v, 2)
    ans += count * (N - v)

print(ans)
