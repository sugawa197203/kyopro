import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

debug = lambda *x: print(*x, file=sys.stderr)

a = list(map(int, input().split()))

if len(set(a)) == 1:
	print(2)
	exit()

if len(set(a)) == 2:
	for _a in a:
		if a.count(_a) == 2:
			print(2)
			exit()
	print(1)
	exit()

if len(set(a)) == 3:
	print(1)
	exit()

print(0)
