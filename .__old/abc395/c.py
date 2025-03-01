N = int(input())
A = list(map(int, input().split()))

dist = [1000000] * (1000000 + 1)
lastpos = [-1] * (1000000 + 1)

for i, a in enumerate(A):
	if lastpos[a] == -1:
		lastpos[a] = i
	else:
		dist[a] = min(dist[a], i - lastpos[a] + 1)
		lastpos[a] = i

m = min(dist)
print(m if m < 1000000 else -1)
