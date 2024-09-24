import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

sheet = [[0] * 100 for _ in range(100)]

N = int(input())

for i in range(N):
	a, b, c, d = map(int, input().split())
	for j in range(a, b):
		for k in range(c, d):
			sheet[j][k] = 1

print(np.sum(sheet))
