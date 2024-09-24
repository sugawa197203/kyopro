import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N = int(input())
A = list(map(int, input().split()))

_A = list(set(A))
_A.sort()
print(_A[-2])
