import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools


def comb(n, r):
    if n < r:
        return 0
    r = min(r, n - r)
    numerator = 1
    denominator = 1
    for i in range(r):
        numerator *= n - i
        denominator *= i + 1
    return numerator // denominator

print(comb(5, 2))