import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N, M = map(int, input().split())

ABXY = []

for i in range(M):
	a, b, x, y = map(int, input().split())
	ABXY.append((a, b, x, y))

pos = []
pos.append((0, 0))


