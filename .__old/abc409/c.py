N, L = map(int, input().split())
D = list(map(int, input().split()))

if L % 3 != 0:
	print(0)
	exit()

circle = [0] * L

circle[0] = 1
pos = 0
for i in range(N - 1):
	pos += D[i]
	pos %= L
	circle[pos] += 1


ans = 0
for i in range(L // 3):
	a = circle[i]
	b = circle[(i + (L // 3)) % L]
	c = circle[(i + (2 * L // 3)) % L]

	if a >= 1 and b >= 1 and c >= 1:
		ans += a * b * c

print(ans)