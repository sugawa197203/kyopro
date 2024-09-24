import copy
N = int(input())

A = []

for i in range(N):
	A.append(list(input()))


_A = copy.copy(A)

for i in range(N - 1):
	print(A[i][i + 1], A[0][i])
	_A[0][i + 1] = A[0][i]

# for i in range(N - 1):
# 	_A[i + 1][N - 1] = A[i][N - 1]

# for i in range(1, N):
# 	_A[N - 1][i - 1] = A[N - 1][i]

# for i in range(1, N):
# 	_A[i - 1][0] = A[i][0]

for i in range(N):
	for j in range(N):
		print(_A[i][j], end = '')
	print()