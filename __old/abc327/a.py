import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N = int(input())
S = input()

if "ab" in S or "ba" in S:
	print("Yes")
else:
	print("No")