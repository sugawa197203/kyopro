import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

X, Y = map(int, input().split())

if X - Y > 0:
	if X - Y <= 3:
		print("Yes")
		sys.exit()
if Y - X > 0:
	if Y - X <= 2:
		print("Yes")
		sys.exit()
print("No")