N, M, Q = map(int, input().split())

onePermutation = [set() for i in range(N)]
allPermutation = [False] * N

for q in range(Q):
	a, *b = map(int, input().split())
	if a == 1:
		onePermutation[b[0] - 1].add(b[1])
	elif a == 2:
		allPermutation[b[0] - 1] = True
	elif a == 3:
		if allPermutation[b[0] - 1]:
			print("Yes")
		else:
			if b[1] in onePermutation[b[0] - 1]:
				print("Yes")
			else:
				print("No")
