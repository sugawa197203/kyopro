N, K = map(int, input().split())
A = list(map(int, input().split()))

max_a = max(A)
tmp = [0] * (max_a + 1)
for x in A:
	tmp[x] += 1

cnt = [0] * (max_a + 1)
for i in range(1, max_a + 1):
	for j in range(i, max_a + 1, i):
		cnt[i] += tmp[j]

valid = [False] * (max_a + 1)
for i in range(1, max_a + 1):
	if cnt[i] >= K:
		valid[i] = True

ans = [0] * (max_a + 1)
for i in range(1, max_a + 1):
	if valid[i]:
		for j in range(i, max_a + 1, i):
			ans[j] = max(ans[j], i)

for x in A:
	print(ans[x])
