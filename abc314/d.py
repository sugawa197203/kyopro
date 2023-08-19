import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N = int(input())
S = input()
S = list(S)
Q = int(input())

# upper: 0, lower: 1, none: 2
to = 2

change = []

for i in range(Q):
	t, x, c = input().split(" ")

	if t == "1":
		change.append((int(x), c))
		continue

	to = 0 if t == "3" else 1

	for _x, _c in change:
		S[_x - 1] = _c

	change = []

S = "".join(S)

if to == 0:
	S = S.upper()
elif to == 1:
	S = S.lower()

S = list(S)

for _x, _c in change:
	S[_x - 1] = _c

print("".join(S))
