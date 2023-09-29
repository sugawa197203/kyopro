import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N, M, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
l, r = [], []
for i in range(Q):
	tmp = list(map(int, input().split()))
	l.append(tmp[0])
	r.append(tmp[1])
