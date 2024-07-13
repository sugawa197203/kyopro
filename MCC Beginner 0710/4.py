N, K = map(int, input().split())
A = list(map(int, input().split()))

A = set(A)
A = list(A)
A.sort()
if A[0] != 0:
	print(0)
	exit()

if len(A) == 1:
	print(A[0] + 1)
	exit()

for i in range(1, K):
	if A[i] - A[i - 1] > 1:
		print(A[i - 1] + 1)
		exit()

print(A[K-1] + 1)