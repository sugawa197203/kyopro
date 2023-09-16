import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

S = input()
c = 1
for i in range(1, len(S)):
	length = i + 1	
	for j in range(len(S) - length + 1):
		if S[j:j+length] == S[j:j+length][::-1]:
			c = length
print(c)