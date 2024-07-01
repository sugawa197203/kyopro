N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))
hako:dict[list[int]] = dict()
cost = 0
for i in range(N):
	hako[i] = []
for i in range(N):
	hako[A[i]-1].append(W[i])
for i in range(N):
	hako[i].sort(reverse=True)
for i in range(N):
	if len(hako[i]) > 1:
		cost += sum(hako[i][1:])
print(cost)