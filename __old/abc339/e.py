N, D = map(int, input().split())
A = list(map(int, input().split()))

maxlen = 0

j = 0
for i in range(N):
	while j < N and abs(A[j+1] - A[j]) <= D:
		j += 1
	maxlen = max(maxlen, j - i)

print(maxlen)
