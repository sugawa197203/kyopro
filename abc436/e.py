N = int(input())
P = list(map(int, input().split()))

invP = [0] * N
for i, p in enumerate(P):
	invP[p - 1] = i + 1

cycles = {}

watched = [False] * N

for i in range(N):
	if watched[i]:
		continue

	if P[i] == i + 1:
		cycles[i + 1] = [i + 1]
		watched[i] = True
		continue

	cycle = []
	cur = i
	while not watched[cur]:
		watched[cur] = True
		cycle.append(cur + 1)
		cur = P[cur] - 1

	cycles[cycle[0]] = cycle

print(cycles)

ans = 0

for cycle in cycles.values():
	L = len(cycle)
	ans += L * (L + 1) // 2

print(ans)
