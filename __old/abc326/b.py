import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

s = input()

while True:
	_s = int(s)
	_100 = int(s[0])
	_10 = int(s[1])

	if _100 * _10 == int(s[2]):
		print(s)
		sys.exit()

	_s += 1
	s = str(_s)