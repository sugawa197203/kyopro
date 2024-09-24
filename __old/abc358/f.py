N, M, K = map(int, input().split())

G = [[0] * M for _ in range(N)]

nm = N * M

if K < N:
	print("No")
	exit()
