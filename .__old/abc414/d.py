N, M = map(int, input().split())
X = list(map(int, input().split()))

X.sort()
diffX = [(X[i] - X[i-1], X[i], X[i-1]) for i in range(1, N)]
diffX.sort(key=lambda x: x[0])

# union-find structure
parent = list(range(N))
rank = [0] * N
def find(x):
	if parent[x] != x:
		parent[x] = find(parent[x])
	return parent[x]
def union(x, y):
	x_root = find(x)
	y_root = find(y)
	if x_root != y_root:
		if rank[x_root] < rank[y_root]:
			parent[x_root] = y_root
		elif rank[x_root] > rank[y_root]:
			parent[y_root] = x_root
		else:
			parent[y_root] = x_root
			rank[x_root] += 1

for i in range(N - 1 - M):
		
		


print(diffX)

