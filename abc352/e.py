from atcoder.dsu import DSU

N, M = map(int, input().split())
K, C = [], []
A = []

dsu = DSU(N)
for i in range(M):
	k, cost = map(int, input().split())
	K.append(k)
	C.append(cost)
	v = list(map(int, input().split()))
	A.append(v)