from collections import defaultdict, deque

N, M = map(int, input().split())

if M == 0:
	print(-1)
	exit()

G = defaultdict(list)
NodeXorTable = [[False] * (2**10) for _ in range(N)]
for _ in range(M):
	u, v, w = map(int, input().split())
	u -= 1
	v -= 1
	G[u].append((v, w))

queue = deque([(0, 0)])
NodeXorTable[0][0] = True

while queue:
	u, xor = queue.popleft()
	for v, w in G[u]:
		new_xor = xor ^ w
		if not NodeXorTable[v][new_xor]:
			NodeXorTable[v][new_xor] = True
			queue.append((v, new_xor))

NTable = NodeXorTable[-1]

for i in range(2**10):
	if NTable[i]:
		print(i)
		exit()
print(-1)
