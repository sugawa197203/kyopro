import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N = input()

b = int(N[0])
if len(N) == 1:
	print("Yes")
	sys.exit()
for s in N[1:]:
	n = int(s)
	if n >= b:
		print("No")
		sys.exit()
	b = n
print("Yes")


