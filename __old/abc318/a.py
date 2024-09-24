import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools


N, M, P = map(int, input().split())

a = N - M
print(a // P + 1)