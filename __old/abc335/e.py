N, M = map(int, input().split())
A = list(map(int, input().split()))
U, V = [], []
for i in range(M):
	u, v = map(int, input().split())
	U.append(u)
	V.append(v)

vertex = [(i, a) for i, a in enumerate(A)]
conections = []
for i in range(N):
	conect = []
	for j in range(M):
		if U[j] == i or V[j] == i:
			conect.append(j)
	conections.append(conect)

table = sorted(vertex, key=lambda x: x[1])
droped = [False] * N
for i in range(N):

	value = table[i]

	connected = []
	for j in range(M):
		if conection[j][0] == value[0] or conection[j][1] == value[0]:
			connected.append(conection[j])
