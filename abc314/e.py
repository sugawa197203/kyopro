import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N, M = map(int, input().split(" "))
C = []
P = []
S = []

for i in range(N):
	buf = list(map(int, input().split(" ")))
	C.append(buf[0])
	P.append(buf[1])
	S.append(buf[2:])

costpers = []

for i, s in enumerate(S):
	print(s)
	avg = sum(s) / len(s)
	costpers.append(avg / C[i])

COSTPER = sum(costpers) / len(costpers)

print(COSTPER)
print(M / COSTPER)
