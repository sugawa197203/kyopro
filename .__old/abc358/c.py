import itertools

N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
minimum = 999999
for pattern in list(itertools.product([True, False], repeat=N)):
	get = [False] * M
	for i in range(N):
		if pattern[i]:
			for j in range(M):
				get[j] |= S[i][j] == 'o'
	if all(get):
		minimum = min(minimum, sum(pattern))

print(minimum)
