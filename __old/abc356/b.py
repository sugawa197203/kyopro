N, M = map(int, input().split())
A = list(map(int, input().split()))
_A = [0] * M

for i in range(N):
	X = list(map(int, input().split()))
	for i, x in enumerate(X):
		_A[i] += x

for a, _a in zip(A, _A):
	if a > _a:
		print("No")
		exit()

print("Yes")