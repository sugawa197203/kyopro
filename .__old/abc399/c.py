N, M = map(int, input().split())

if M == 0:
	print(0)
	exit()

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent, rank):
    rx = find(x, parent)
    ry = find(y, parent)
    if rx == ry:
        return False
    if rank[rx] < rank[ry]:
        parent[rx] = ry
    else:
        parent[ry] = rx
        if rank[rx] == rank[ry]:
            rank[rx] += 1
    return True

parent = [i for i in range(N)]
rank = [0] * N
comp = N
for _ in range(M):
	u, v = map(int, input().split())
	u -= 1
	v -= 1
	if union(u, v, parent, rank):
		comp -= 1
print(M - (N - comp))