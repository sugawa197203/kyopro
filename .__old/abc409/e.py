N = int(input())
x = list(map(int, input().split()))

if all(xi == 0 for xi in x):
	print(0)
	exit()

from collections import defaultdict, deque

Tree = defaultdict(list)

for i in range(N - 1):
	u, v , w = map(int, input().split())
	Tree[u].append((v, w))
	Tree[v].append((u, w))

contains = set(range(1, N + 1))

def GetLeaf(G:defaultdict[list]) -> list:
	leaf = []
	m = 1
	q = deque([m])
	visited = set([m])
	if len(G[m]) == 1:
		leaf.append(m)

	while q:
		node = q.popleft()
		is_leaf = True
		for neighbor, _ in G[node]:
			if neighbor not in visited:
				is_leaf = False
				visited.add(neighbor)
				q.append(neighbor)
		if is_leaf:
			leaf.append(node)

	return leaf

ans = 0
leaf = set(GetLeaf(Tree))
print(f"{leaf=}")
while len(contains) > 1:
	if not leaf:
		break
	
	movecost = []
	for l in leaf:
		nighbor, cost = Tree[l][0]
		movecost.append((abs(x[l - 1] * cost), l))
	movecost.sort()
	print(f"{movecost=}")
	cost, move = movecost[0]
	ans += cost
	parent = Tree[move][0][0]
	Tree[parent] = [(n, c) for n, c in Tree[parent] if n != move]

	del Tree[move]
	leaf.remove(move)
	leaf.add(parent)
	contains.remove(move)
	print(f"{Tree=}")
	print(f"{leaf=}")
	print("dell", move)
	x[parent - 1] += x[move - 1]
	

print(ans)
