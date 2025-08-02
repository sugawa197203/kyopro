from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

count = defaultdict(int)

for j in range(N):
	_j = j - A[j]
	if 0 <= _j:
		count[_j] += 1

ans = 0
for i in range(N):
	ans += count.get(i + A[i], 0)

print(ans)
