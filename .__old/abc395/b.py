N = int(input())

import math

_N = int(math.ceil(N / 2))

ans = [["" for _ in range(N)] for _ in range(N)]

for i in range(_N):

	char = "#" if i % 2 == 0 else "."
	for j in range(i, N - i):
		ans[i][j] = char
		ans[N - 1 - i][j] = char
	for j in range(i, N - i):
		ans[j][i] = char
		ans[j][N - 1 - i] = char

print("\n".join(["".join(a) for a in ans]))
