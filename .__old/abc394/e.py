N = int(input())

G:dict[list[tuple[int, str]]] = dict()
ans = [[-1] * N for _ in range(N)]
for i in range(N):
	G[i] = []
	S = input()
	for j in range(N):
		if i == j:
			ans[i][j] = 0
		if S[j] == '-':
			continue
		if i != j:
			ans[i][j] = 1
		G[i].append((j, S[j]))


RG = dict()
for i in range(N):
	RG[i] = []

for i in range(N):
	for j, c in G[i]:
		RG[j].append((i, c))

print(G)
print(RG)

# dist 2
for i in range(N):
	for j in range(N):
		if ans[i][j] == 1:
			for 


for i in range(N):
	print(' '.join(map(str, ans[i])))
