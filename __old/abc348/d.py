import numpy as np
from queue import Queue
H, W = map(int, input().split())
A = np.array([list(input()) for _ in range(H)])
START = (0, 0)
for i in range(H):
	for j in range(W):
		if A[i, j] == 'S':
			START = (i, j)
			break
GOAL = (H-1, W-1)
for i in range(H):
	for j in range(W):
		if A[i, j] == 'G':
			GOAL = (i, j)
			break
N = int(input())
R, C, E = [], [], []
ITEMINDEX:dict[tuple[int, int], int] = dict()
for i in range(N):
	r, c, e = map(int, input().split())
	R.append(r-1)
	C.append(c-1)
	E.append(e)
	ITEMINDEX[(r-1, c-1)] = i

ITEM = np.zeros((H, W), dtype=int)
for r, c, e in zip(R, C, E):
	ITEM[r, c] = e

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def getItem(_pos:tuple[int, int]) -> int:
	return ITEM[_pos[0], _pos[1]]

def isInGrid(_pos:tuple[int, int]) -> bool:
	return 0 <= _pos[0] < H and 0 <= _pos[1] < W

if not getItem(START) > 0:
	print("No")
	exit()

def getLength(_from:tuple[int, int], _to:tuple[int, int]) -> int:
	__q = Queue()
	__q.put(_from)
	__visited = set()
	__length = 0
	while not __q.empty():
		__length += 1
		__pos = __q.get()
		if __pos == _to:
			return __length
		for __d in directions:
			__next = (__pos[0] + __d[0], __pos[1] + __d[1])
			if isInGrid(__next) and not __next in __visited and A[__next[0], __next[1]] != '#':
				__visited.add(__next)
				__q.put(__next)
	return 10**9

def getItemFromIndex(_index:int) -> tuple[tuple[int, int], int]:
	return (R[_index], C[_index]), E[_index]

usedItemIndex:set[int] = set()
STATE_STACK:list[tuple[tuple[int, int], int]] = []
STATE_STACK.append((START, getItem(START)))

while len(STATE_STACK) > 0:
	__pos, __enegy = STATE_STACK.pop()
	usedItemIndex.add(ITEMINDEX[__pos])
	if __pos == GOAL:
		print("Yes")
		exit()
	for __i in ITEMINDEX.values():
		if not __i in [i for v, i in STATE_STACK]:
			__ipos, __ienegy = getItemFromIndex(__i)
			__length = getLength(__pos, __ipos)
			if __length <= __enegy:
				STATE_STACK.append((__ipos, __ienegy))
				
print("No")
