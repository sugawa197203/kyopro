from itertools import product
import numpy as np
from copy import deepcopy
from collections import deque
class HopcroftKarp:
	def __init__(self, N0, N1):
		self.N0 = N0
		self.N1 = N1
		self.N = N = 2+N0+N1
		self.G = [[] for i in range(N)]
		for i in range(N0):
			forward = [2+i, 1, None]
			forward[2] = backward = [0, 0, forward]
			self.G[0].append(forward)
			self.G[2+i].append(backward)
		self.backwards = bs = []
		for i in range(N1):
			forward = [1, 1, None]
			forward[2] = backward = [2+N0+i, 0, forward]
			bs.append(backward)
			self.G[2+N0+i].append(forward)
			self.G[1].append(backward)
 
	def add_edge(self, fr, to):
		#assert 0 <= fr < self.N0
		#assert 0 <= to < self.N1
		v0 = 2 + fr
		v1 = 2 + self.N0 + to
		forward = [v1, 1, None]
		forward[2] = backward = [v0, 0, forward]
		self.G[v0].append(forward)
		self.G[v1].append(backward)
 
	def bfs(self):
		G = self.G
		level = [None]*self.N
		deq = deque([0])
		level[0] = 0
		while deq:
			v = deq.popleft()
			lv = level[v] + 1
			for w, cap, _ in G[v]:
				if cap and level[w] is None:
					level[w] = lv
					deq.append(w)
		self.level = level
		return level[1] is not None
 
	def dfs(self, v, t):
		if v == t:
			return 1
		level = self.level
		for e in self.it[v]:
			w, cap, rev = e
			if cap and level[v] < level[w] and self.dfs(w, t):
				e[1] = 0
				rev[1] = 1
				return 1
		return 0
 
	def flow(self):
		flow = 0
		G = self.G
		bfs = self.bfs; dfs = self.dfs
		while bfs():
			*self.it, = map(iter, G)
			while dfs(0, 1):
				flow += 1
		return flow
 
	def matching(self):
		return [cap for _, cap, _ in self.backwards]

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
ans = 0
HC = HopcroftKarp(H * W, H * W)
oddflag = True
DXY = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# bit全探索
for mask in product((0, 1), repeat=H * W):
	# oddflag = not oddflag
	# if oddflag:
	# 	continue

	hc = deepcopy(HC)
	# mask = np.array(mask).reshape(H, W)
	for x, y in product(range(H), range(W)):
		if mask[x + y * H] == 0:
			for dx, dy in DXY:
				nx, ny = x + dx, y + dy
				if 0 <= nx < H and 0 <= ny < W and mask[nx + ny * H] == 0:
					if x % 2 == 0:
						if y % 2 == 0:
							hc.add_edge(x + y * H, nx + ny * H)
						else:
							hc.add_edge(nx + ny * H, x + y * H)
					else:
						if y % 2 == 0:
							hc.add_edge(nx + ny * H, x + y * H)
						else:
							hc.add_edge(x + y * H, nx + ny * H)

	zerocount = 0
	for x, y in product(range(H), range(W)):
		if mask[x + y * H] == 0:
			zerocount += 1
	if hc.flow() * 2 != zerocount:
		continue

	_ans = 0
	for x, y in product(range(H), range(W)):
		if mask[x + y * H] == 0:
			_ans ^= A[x][y]
	ans = max(ans, _ans)
print(ans)
