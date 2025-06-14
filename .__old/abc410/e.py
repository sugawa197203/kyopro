N, H, M = map(int, input().split())
AB = []
for _ in range(N):
	a, b = map(int, input().split())
	AB.append((a, b))

dp = [[-1] * (H + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(1, N + 1):
	a, b = AB[i - 1]
	for j in range(H + 1):
		dp[i][j] = dp[i - 1][j]  # Not taking the i-th item
		if j >= a and dp[i - 1][j - a] != -1:
			dp[i][j] = max(dp[i][j], dp[i - 1][j - a] + b)
ans = -1
for j in range(H + 1):
	if dp[N][j] >= M:
		ans = j
		break
if ans == -1:
	print(-1)