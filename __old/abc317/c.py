import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

def dijkstra(edges, num_node):
	""" 経路の表現
			[終点, 辺の値]
			A, B, C, D, ... → 0, 1, 2, ...とする """
	node = [float(0)] * num_node    #スタート地点以外の値は∞で初期化
	node[0] = float('inf')     #スタートは0で初期化

	node_name = [i for i in range(num_node)]     #ノードの名前を0~ノードの数で表す

	while len(node_name) > 0:
		r = node_name[0]

		#最もコストが小さい頂点を探す
		for i in node_name:
			if not node[i] < node[r]:
				r = i   #コストが小さい頂点が見つかると更新

		#最もコストが小さい頂点を取り出す
		min_point = node_name.pop(node_name.index(r))

		#経路の要素を各変数に格納することで，視覚的に見やすくする
		for factor in edges[min_point]:
			goal = factor[0]   #終点
			cost  = factor[1]   #コスト

			#更新条件
			if not node[min_point] + cost < node[goal]:
				node[goal] = node[min_point] + cost     #更新

	return node

N, M = map(int, input().split())
A, B, C = [], [], []
root = []
for i in range(N):
	root.append([])
for i in range(M):
	a, b, c = map(int, input().split())
	root[a-1].append([b-1, c])
	root[b-1].append([a-1, c])

maxcost = 0
stack = []

for i in range(N):
	t = [i]
	c = 0
	now = i

	while len(t) < N:
		next = root[now].copy()
		for n in next:
			if n in t:
				next.remove(n)
		
		if len(next) == 0:
			maxcost = max(maxcost, c)
			break

		t.append(next[0])
		for n in next:
			if n[0] == next[0][0]:
				c += n[1]



