N = int(input())
C = list(map(int, input().split()))
A = list(map(int, input().split()))
dp = [float('inf')] * (N)
dp[N - 1] = 0
cnt = 0
for i in range(N - 1, -1, -1):
	if 0 <= A[i - 1]:
		for c in range(C[i - 1]):
			dp[i - c - 1] = min(dp[i - c - 1], dp[i] + 1)

print(dp[0]) 
print(dp)
