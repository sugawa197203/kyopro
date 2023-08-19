import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N = int(input())

FS = []

for i in range(N):
	f, s = map(int, input().split())
	FS.append((f, s))

FS = sorted(FS, key=lambda x: x[1], reverse=True)

key, maxi = FS.pop(0)
_key, _maxi = FS.pop(0)

if not key == _key:
	print(maxi + _maxi)
	sys.exit()
else:
	v = maxi + _maxi // 2

for _k, _m in FS:
	if maxi + _m <= v:
		print(v)
		sys.exit()
	if not _k == key:
		_v = maxi + _m
		print(max(v, _v))
		sys.exit()

print(v)

