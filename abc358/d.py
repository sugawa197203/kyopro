N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
Ai = 0
Bi = 0
cost = 0

for b in B:
	if Ai >= N:
		print(-1)
		exit()
	while A[Ai] < b:
		Ai += 1
		if Ai >= N:
			print(-1)
			exit()
	cost += A[Ai]
	Ai += 1

print(cost)