import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N, K, H, W, Q = map(int, input().split())
p, q, u, v, r = [], [], [], [], []
for i in range(N):
	tmp = list(map(int, input().split()))
	p.append(tmp[0])
	q.append(tmp[1])
	u.append(tmp[2])
	v.append(tmp[3])
	r.append(tmp[4])
X, Y = [], []
for i in range(Q):
	x, y = map(int, input().split())
	X.append(x)
	Y.append(y)
