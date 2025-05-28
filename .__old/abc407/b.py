X, Y = map(int, input().split())

n = 36

cnt = 0

for a in range(1, 7):
	for b in range(1, 7):
		if a + b >= X:
			cnt += 1
		elif abs(a - b) >= Y:
			cnt += 1

print(cnt / 36)