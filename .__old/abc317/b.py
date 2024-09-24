import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N = int(input()) + 1
A = list(map(int, input().split()))
A.sort()
print(int(1/2*N*(A[0] + A[-1]) - sum(A)))
