import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N, M, P = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

product = itertools.product(A, B)
result = []
for a, b in product:
	result.append(min(a + b, P))

print(sum(result))
