import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N = int(input())
S = list(input())

ans = set()

ans = dict()
for alp in "abcdefghijklmnopqrstuvwxyz":
	ans[alp] = 0

i = 0
_s = ""
for s in S:
	if _s == s:
		i += 1
	else:
		i = 1
	_s = s
	ans[s] = max(ans[s], i)

sum = 0
for v in ans.values():
	sum += v

print(sum)