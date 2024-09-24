import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N = int(input())
A = list(map(int, input().split()))

print(A[0], end=" ")
b = A[0]
for a in A[1:]:
	if a > b:
		for i in range(b+1, a):
			print(i, end=" ")
	else:
		for i in range(b-1, a, -1):
			print(i, end=" ")
	print(a, end=" ")
	b = a

