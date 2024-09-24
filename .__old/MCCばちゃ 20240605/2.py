N = int(input())
A = map(int, input().split())
_A = list(range(N))
result = [0] * N
for i, a in enumerate(A):
	if a == -1:
		result[0] = i + 1
	result[a - 1] = i + 1

print(*result)
