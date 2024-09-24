import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N = int(input())
X, Y, Z = [], [], []

for i in range(N):
	x, y, z = map(int, input().split())
	X.append(x)
	Y.append(y)
	Z.append(z)

WINS = []
Chair = 0
MaxChair = sum(Z)
for i in range(N):
	WINS.append(X[i] > Y[i])
	if WINS[i]:
		Chair += Z[i]

if Chair > MaxChair/2:
	print("0")
	sys.exit()

mores = []
for i in range(N):
	if not WINS[i]:
		mores.append(Y[i]-X[i])
	else:
		mores.append(0)

print(mores)
print((sum(mores) + 1))
print((sum(mores) + 1) // 2)
