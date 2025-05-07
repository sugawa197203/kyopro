N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]

sabun0 = 0
sabun90 = 0
sabun180 = 0
sabun270 = 0

# sabun0
for i in range(N):
	for j in range(N):
		if S[i][j] != T[i][j]:
			sabun0 += 1

# sabun90
for i in range(N):
	for j in range(N):
		if S[i][j] != T[j][N - 1 - i]:
			sabun90 += 1

# sabun180
for i in range(N):
	for j in range(N):
		if S[i][j] != T[N - 1 - i][N - 1 - j]:
			sabun180 += 1

# sabun270
for i in range(N):
	for j in range(N):
		if S[i][j] != T[N - 1 - j][i]:
			sabun270 += 1

print(min(sabun0, sabun90 + 1, sabun180 + 2, sabun270 + 3))