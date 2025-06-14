N, Q = map(int, input().split())
X = list(map(int, input().split()))
ans = []
box = [0] * (N + 1)
box[0] = 1000000

def minindex():
	m = min(box)
	for i in range(N + 1):
		if box[i] == m:
			return i

for x in X:
	if x > 0:
		ans.append(x)
		box[x] += 1
	else:
		m = minindex()
		box[m] += 1
		ans.append(m)

print(*ans)