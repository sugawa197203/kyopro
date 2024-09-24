import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

S = input()

for s in S:
	if s in 'aiueo':
		continue
	print(s, end='')
