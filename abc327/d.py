import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

bufgraph = []

for a, b in zip(A, B):
	if a == b:
		print("No")
		exit()
	bufgraph.append((a, b) if a < b else (b, a))

bufgraph.sort()

graph = []
buf = None
b = -1
for bg in bufgraph:
	if b != bg[0]:
		buf = []
		b = bg[0]
		if buf != None:
			graph.append(buf)
	if not bg in buf:
		buf.append(bg)

checked = [False] * N

length = [0] * N

for gnum in graph:
	for _g in gnum:
		g = (_g[0] - 1, _g[1] - 1)
		if checked[g[1]] and checked[g[0]] and ((length[g[0]] + length[g[1]]) % 2 == 1):
			print("No")
			exit()
		checked[g[0]] = True
		checked[g[1]] = True
		length[g[1]] = 1 + length[g[0]]

print("Yes")