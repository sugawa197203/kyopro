import numpy as np
import math
import sys
import collections
import bisect
import copy

N = int(input())
A = []

for i in range(N):
	input()
	a = list(map(int, input().split(" ")))
	A.append(a)

X = int(input())

WIN = []

for i, a in enumerate(A):
	if X in a:
		WIN.append(i)

MINLEN = 1000000000

for w in WIN:
	if len(A[w]) < MINLEN:
		MINLEN = len(A[w])

MINWIN = filter(lambda x: len(A[x]) == MINLEN, WIN)
MINWIN = list(MINWIN)

print(len(MINWIN))
for w in MINWIN:
	print(w+1, end=" ")
