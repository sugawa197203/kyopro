N, M = map(int, input().split(" "))
A = []
B = []

for i in range(M):
	a, b = map(int, input().split(" "))

	A.append(a)
	B.append(b)



graf = [[0] * N for i in range(N)]

for i in range(M):
	graf[A[i] - 1][B[i] - 1] = 1

print(graf)



