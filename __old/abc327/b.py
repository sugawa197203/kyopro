import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

B = int(input())

for i in range(1, 1001):
	if i ** i == B:
		print(i)
		exit()
	if i ** i > 10 ** 18:
		break

print(-1)

