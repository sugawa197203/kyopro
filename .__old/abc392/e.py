N, M = map(int, input().split())
A, B = [], []
from collections import defaultdict
conectCount = defaultdict(int)
cable = dict()
for i in range(M):
	a, b = map(int, input().split())
	A.append(a)
	B.append(b)
	if a < b:
		a, b = b, a
	conectCount[(a, b)] += 1
	cable[(a, b)] = i

import sys
sys.setrecursionlimit(10**9)

unionFind = [i for i in range(N)]

def root(x:int) -> int:
	if unionFind[x] == x:
		return x
	unionFind[x] = root(unionFind[x])
	return unionFind[x]

def unite(x:int, y:int) -> None:
	x = root(x)
	y = root(y)
	if x == y:
		return
	unionFind[x] = y

for i in range(M):
	a, b = A[i], B[i]
	unite(a-1, b-1)
	print(unionFind)
import bisect
# print(unionFind)
networks = list(set(unionFind))
stepCount = len(networks)
# print(networks)
# print(stepCount - 1)
joucho:dict[int, dict[int]] = dict()
for ck, cv in conectCount.items():
	a, b = ck
	if a == b or cv > 1:
		if unionFind[a-1] not in joucho:
			joucho[unionFind[a-1]] = dict()
		joucho[unionFind[a-1]][(a, b)] = cv

# print(joucho)

horyu = 0
ans = []
print(networks, unionFind)
while len(networks) > 1:
	# print(networks)
	network = networks.pop(horyu)
	if network not in joucho:
		networks.add(network)
		horyu += 1
		continue
	if len(joucho[network].keys()) > 0:
		front = list(joucho[network].keys()).pop(0)
		_cable = cable[front]
		a, b = front
		uniconRight = bisect.bisect_right(unionFind, network)
		delnetwork = unionFind[uniconRight]
		delfright = bisect.bisect_right(unionFind, delnetwork)
		server = delnetwork
		# print(_cable, a, server)
		ans.append((_cable+1, a, server))
		joucho[network][front] -= 1
		if joucho[network][front] == 0:
			joucho[network].pop(front)

		for i in range(uniconRight, delfright):
			if unionFind[i] == delnetwork:
				unionFind[i] = network
		
		print(unionFind)
		networks.remove(delnetwork)
		print(networks)
		print(joucho)

print("ans")
print(len(ans))
for a in ans:
	print(*a)