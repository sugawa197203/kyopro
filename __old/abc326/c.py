import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
count = 0

for a in A:
	first = bisect.bisect_left(A, a)
	last = bisect.bisect_left(A, a + M)
	count = max(count, last - first)

print(count)
