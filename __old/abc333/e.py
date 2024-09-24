import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N = int(input())

T, X = [], []

for i in range(N):
	t, x = map(int, input().split())
	T.append(t)
	X.append(x)


