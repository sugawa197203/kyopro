N = int(input())
A, C = [], []
for _ in range(N):
	a, c = map(int, input().split())
	A.append(a)
	C.append(c)

cost:dict[int] = dict()

for a, c in zip(A, C):
	cost[c] = min(cost.get(c, 10**9), a)

maxcost = max(cost.values())
print(maxcost)
