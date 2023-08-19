import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

A, B = map(int, input().split())

q, m = divmod(A, B)

if m == 0:
	print(q)
else:
	print(q+1)
