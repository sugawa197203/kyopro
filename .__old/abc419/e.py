from heapq import heappush, heappop, heapify
from copy import deepcopy

N, M, L = map(int, input().split())
A = list(map(int, input().split()))

sub = [0] * (N - L + 1)
sub[0] = sum(A[:L])
for i in range(1, N - L + 1):
    sub[i] = sub[i - 1] - A[i - 1] + A[i + L - 1]
state = [[[0] * N, sub.copy()] for _ in range(N)]

for i in range(N):
    state[i][0][i] = 1
    for j in range(min(i, max(i - L + 1, 0)), min(i + 1, N - L + 1)):
        state[i][1][j] += 1

pq = []
for s in state:
    c = sum(M - x)

for s in state:
    print(s)

state = heapify(state)
