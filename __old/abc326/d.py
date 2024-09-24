import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N = int(input())
R = input()
C = input()

ABC = [['.' for i in range(N)] for j in range(N)]

if R[0] != C[0]:
	print("No")
	sys.exit()

if len(list(set(R))) != 3:
	print("No")
	sys.exit()

if len(list(set(C))) != 3:
	print("No")
	sys.exit()

def includeTate(moji, i):
	for j in range(N):
		if ABC[j][i] == moji:
			return True
	return False

def includeYoko(moji, i):
	for j in range(N):
		if ABC[i][j] == moji:
			return True
	return False

i = 0
for r, c in zip(R, C):
	if r == c:
		ABC[i][i] = r
	else:
		for j in range(N):
			if not includeYoko(c, j) and ABC[i][j] == '.':
				ABC[j][i] = c
				break
		for j in range(N):
			if not includeTate(r, j) and ABC[j][i] == '.':
				ABC[i][j] = r
				break
	i += 1

def okyoko(i):
	a, b, c = False, False, False
	for j in range(N):
		if ABC[i][j] == 'A':
			a = True
		elif ABC[i][j] == 'B':
			b = True
		elif ABC[i][j] == 'C':
			c = True
	return a and b and c

def oktate(i):
	a, b, c = False, False, False
	for j in range(N):
		if ABC[j][i] == 'A':
			a = True
		elif ABC[j][i] == 'B':
			b = True
		elif ABC[j][i] == 'C':
			c = True
	return a and b and c

def tarinaiyoko(i):
	tarinai = ""
	for j in range(N):
		if ABC[i][j] == 'A':
			tarinai += 'A'
		if ABC[i][j] == 'B':
			tarinai += 'B'
		if ABC[i][j] == 'C':
			tarinai += 'C'
	return tarinai

def tarinaitate(j):
	tarinai = ""
	if not includeTate('A', j):
		tarinai += 'A'
	if not includeTate('B', j):
		tarinai += 'B'
	if not includeTate('C', j):
		tarinai += 'C'
	return tarinai


for i in range(N):
	tarinai = tarinaitate(i)
	for t in tarinai:
		for j in range(N):
			if not includeYoko(t, j) and ABC[i][j] == '.':
				ABC[j][i] = t
				break
		
print("Yes")
for i in range(N):
	print("".join(ABC[i]))
