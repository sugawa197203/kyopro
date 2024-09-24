import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools


N = int(input())

def maxf(i, l, n):
	_l = []
	for _i in range(n):
		if i - 1 <= _i <= i + 1:
			continue
		_l.append(l[_i])
	if len(_l) == 0:
		return l[0]
	return max(_l)

table = [[0] * N for _ in range(N)]
table[0] = list(map(int, input().split()))

for i in range(N - 1):
	l = list(map(int, input().split()))
	for j in range(N):
		table[i + 1][j] += maxf(j, l, len(l))

print(table)


