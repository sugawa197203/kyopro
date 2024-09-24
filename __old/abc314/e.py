import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N, M = map(int, input().split())
r = [list(map(int, input().split())) for _ in range(N)]

z = [r[i].count(0) for i in range(N)]
dp = [0] * (M + 1)

for i in range(M - 1, -1, -1):
	mn = float('inf')
	for j in range(N):
		c, p, *S = r[j]
		ret = c
		for s in S:
			ret += dp[min(i + s, M)] / p
		ret *= p / (p - z[j])
		mn = min(mn, ret)
	dp[i] = mn
print(dp[0])
