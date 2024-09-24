N, M = map(int, input().split())
a = [0] * N
c = 1
for i in range(M):
	t, x = map(int, input().split())
	if t == 1:
		a[x - 1] += c
	elif t == 2:
		a[x - 1] -= c
	elif t == 3:
		c += 1

for i in range(N):
	if a[i] != 0 and a[i] - c == 0:
		print(i + 1)
