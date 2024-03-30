import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

A = [list(map(int, input().split())) for _ in range(9)]

A1 = A.copy()
for i in range(9):
	if len(list(set(A1[i]))) != 9:
		print("No")
		exit()

A2 = np.array(A).T.tolist()

for i in range(9):
	if len(list(set(A2[i]))) != 9:
		print("No")
		exit()

# split 3 * 3 * 3 and check 1 group has 1~9
A3 = []
for i in range(3):
	for j in range(3):
		A3.append(A[i*3][j*3:(j+1)*3] + A[i*3+1][j*3:(j+1)*3] + A[i*3+2][j*3:(j+1)*3])

for i in range(9):
	if len(list(set(A3[i]))) != 9:
		print("No")
		exit()

print("Yes")
