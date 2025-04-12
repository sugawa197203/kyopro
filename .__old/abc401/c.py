N, K = map(int, input().split())

A = [1] * (N + 1)
ruiseki = K
if K <= N:
	A[K] = ruiseki
	ruiseki -= A[0]
	ruiseki += A[K]
	if K + 1 <= N:
		A[K + 1] = 2 * K - 1
		ruiseki -= A[1]
		ruiseki += A[K + 1]

	for k in range(K + 2, N + 1):
		A[k] = ruiseki
		ruiseki -= A[k - K]
		ruiseki += A[k]

		ruiseki %= 10**9
	

print(A[N] % (10**9))