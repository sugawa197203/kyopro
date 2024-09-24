import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N, M = map(int, input().split())
K = []
S = []

for i in range(M):
	tmp = list(map(int, input().split()))
	K.append(tmp[0])
	S.append(tmp[1:])

st = [float('inf')] * N
T = []

a = 0
n = N
c = 0
T = []
T.append(N)
_t = set()
e = set()
while True:
	for t in T:
		if t in e:
			continue
		for s in S:
			if t in s:
				for i in s:
					st[i-1] = min(st[i-1], a)
					_t.add(i)
					if i == 1:
						print(st[0])
						sys.exit()
		e.add(t)
	a += 1
	T = list(_t)
	_t = set()
		
