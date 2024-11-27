N, M = map(int, input().split())

import itertools

l = list(range(1, M + 1))

for i in itertools.combinations(l, N):
    print(*i)
