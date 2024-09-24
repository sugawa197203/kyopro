N, M = map(int, input().split())
s = set()
for _ in range(M):
	a, b = map(int, input().split())
	s.add(b)
if len(s) == N - 1:
	print(N * -~N // 2 - sum(s))
else:
	print(-1)
