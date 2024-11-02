import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools
debug = lambda *x: print(x, file=sys.stderr)

N, M = map(int, input().split())
dangerous = set()

for _ in range(M):
	a, b = map(int, input().split())
	l = [(a, b), (a-2, b+1), (a-2, b-1), (a-1, b+2), (a-1, b-2), (a+1, b+2), (a+2, b+1), (a+1, b-2), (a+2, b-1)]
	for x, y in l:
		if 1 <= x <= N and 1 <= y <= N:
			dangerous.add((x, y))
print(N*N - len(dangerous))
