import numpy as np; import sortedcontainers as sc; import math; import bisect; import itertools; import sys; import networkx as nx; debug = lambda *arg : print(*arg, file=sys.stderr);

N = int(input())
K = list(map(int, input().split()))

total_sum = sum(K)
target = total_sum // 2
best_A_sum = 0

dp = [[False] * (target + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(1, N + 1):
    for j in range(target + 1):
        dp[i][j] = dp[i - 1][j]
        if j >= K[i - 1]:
            dp[i][j] = dp[i][j] or dp[i - 1][j - K[i - 1]]

for j in range(target, -1, -1):
    if dp[N][j]:
        best_A_sum = j
        break

B_sum = total_sum - best_A_sum

print(max(best_A_sum, B_sum))
