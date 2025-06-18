N = int(input())
A = list(map(int, input().split()))
K = int(input())

ans = 0
for a in A:
	if a >= K:
		ans += 1

print(ans)