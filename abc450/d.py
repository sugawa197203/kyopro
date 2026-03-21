from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))

modak = deque(sorted(list(set([a % K for a in A]))))
n = len(modak)
minval = 10**10

for _ in range(n):
    minval = min(minval, modak[-1] - modak[0])
    front = modak.popleft()
    front += K
    modak.append(front)

print(minval)

