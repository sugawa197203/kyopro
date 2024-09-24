import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

H, W = map(int, input().split())

HnoneFlag = [False] * H
WnoneFlag = [False] * W


def allSameRow(c, h):
	if HnoneFlag[h]:
		return False
	front = " "
	for w in range(W):
		if not c[h][w] == " ":
			front = c[h][w]
			break

	co = 0
	for _c in c[h]:
		if _c == front:
			co += 1
	if co == 1:
		return False

	for w in range(W):
		if c[h][w] == " ":
			continue
		if not c[h][w] == front:
			return False
	return True


def allSameCol(c, w):
	if WnoneFlag[w]:
		return False

	front = " "
	for h in range(H):
		if not c[h][w] == " ":
			front = c[h][w]
			break

	co = 0
	for _c in c:
		if _c[w] == front:
			co += 1
	if co == 1:
		return False

	for h in range(H):
		if c[h][w] == " ":
			continue
		if not c[h][w] == front:
			return False
	return True


C = []
checkRow = [False] * H
checkCol = [False] * W

for i in range(H):
	C.append(list(input()))

a = 0
while True:
	a += 1
	if a == 10:
		sys.exit()
	for h in range(H):
		if allSameRow(C, h):
			checkRow[h] = True

	for w in range(W):
		if allSameCol(C, w):
			checkCol[w] = True

	if not (any(checkRow) or any(checkCol)):
		count = 0
		for h in range(H):
			for w in range(W):
				if not C[h][w] == " ":
					count += 1
		print(count)
		sys.exit()

	for h in range(H):
		if checkRow[h]:
			for w in range(W):
				C[h][w] = " "
			HnoneFlag[h] = True

	for w in range(W):
		if checkCol[w]:
			for h in range(H):
				C[h][w] = " "
			WnoneFlag[w] = True

	checkCol = [False] * W
	checkRow = [False] * H
