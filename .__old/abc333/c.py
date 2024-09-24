import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N = int(input())

rep = [1,
	   1,
	   1,
	   11,
	   11,
	   11,
	   111,
	   111,
	   111,
	   1111,
	   1111,
	   1111,
	   11111,
	   11111,
	   11111,
	   111111,
	   111111,
	   111111,
	   1111111,
	   1111111,
	   1111111,
	   11111111,
	   11111111,
	   11111111,
	   111111111,
	   111111111,
	   111111111,
	   1111111111,
	   1111111111,
	   1111111111,
	   11111111111,
	   11111111111,
	   11111111111,
	   111111111111,
	   111111111111,
	   111111111111,]

l = []

for i in itertools.combinations(rep, 3):
	l.append(sum(i))

l = list(set(l))
l.sort()
print(l[N-1])

