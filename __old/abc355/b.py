N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

_A = A.copy()
_A.extend(B)
_A.sort()

for i in range(1, N+M):
	if _A[i] in A and _A[i - 1] in A:
		print("Yes")
		exit()

print("No")
