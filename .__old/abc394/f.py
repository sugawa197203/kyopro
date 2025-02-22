N = int(input())
if N <= 4:
	print(-1)
	exit()

from collections import defaultdict

T = defaultdict(list)
for i in range(N-1):
	a, b = map(int, input().split())
	a -= 1
	b -= 1
	T[a].append(b)
	T[b].append(a)

jisumore4count = 0
for i in range(N):
	jisu = len(T[i])
	if 4 <= jisu:
		jisumore4count += 1

if jisumore4count == 0:
	print(-1)
	exit()

jisulist = [0] * N
for i in range(N):
	jisulist[i] = len(T[i])

watched = [False] * N
ans = 0

for i in range(N-1):
	if watched[i]:
		continue

	queue = [i]
	watched[i] = True
	count = 0

	if jisulist[i] != 4 and jisulist[i] != 1:
		continue

	while queue:
		count += 1
		now = queue.pop(0)
		
		if jisulist[now] != 4 and jisulist[now] != 1:
			watched[now] = False
			continue

		for next in T[now]:
			if watched[next]:
				continue
			watched[next] = True

			queue.append(next)

	if 5 <= count:
		ans = max(ans, count)

print(ans)
