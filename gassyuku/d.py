import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N, M = map(int, input().split())
k1 = []
k2 = []
a1 = []
a2 = []
OKlist = [[True] * (N + M) for i in range(N + M)]
for i in range(N):
	tmp = list(map(int, input().split()))
	k1.append(tmp[0])
	a1.append(tmp[1:])

for i in range(M):
	tmp = list(map(int, input().split()))
	k2.append(tmp[0])
	a2.append(tmp[1:])

t1 = [0] * N
t2 = [0] * M

for i, _a1 in enumerate(a1):
	t1[i] += len(_a1)
	for a in _a1:
		t2[a-1-N] += 1

for i, _a in enumerate(a2):
	t2[i] += len(_a)
	for a in _a:
		t1[a-1] += 1

T1 = [(t, i) for i, t in enumerate(t1)]
T2 = [(t, i + N) for i, t in enumerate(t2)]
T = T1 + T2
T.sort()
ban = set()
A = a1 + a2

for i, a in enumerate(A):
	for _a in a:
		OKlist[i][_a-1] = False

while True:
	if len(T) == 0:
		break
	p = T.pop(0)
	if p[1] in ban:
		continue
	for _a in A[p[1]]:
		ban.add(_a)
	
	for i in range(N + M):
		if not OKlist[i][p[1]]:
			ban.add(i)

print(N + M - len(ban) + 1)

