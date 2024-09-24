import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N, H, X = map(int, input().split())
P = list(map(int, input().split()))

sub = X - H

for i, n in enumerate(P):
    if sub <= n:
        print(i+1)
        exit()
