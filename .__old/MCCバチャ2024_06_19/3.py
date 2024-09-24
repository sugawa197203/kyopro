N = int(input())
A = list(map(int, input().split()))

total = sum(A)
ans = 0

for i in range(N-1):
	total -= A[i]
	print(total, A[i], (A[i] * (N - i - 1)))
	ans += abs(total - (A[i] * (N - i - 1)))

print(ans)