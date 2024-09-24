import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

A, M, L, R = map(int, input().split())

R -= L
A -= L
L = 0

m = A % M
R -= m
c = R // M + 1

print(c)