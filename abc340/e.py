N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = 0

for i in range(1, M+1):
	hand = A[B[i-1]]
	A[B[i-1]] = 0
	
	print(hand, A)
	while hand > 0:
		C += 1
		A[(B[i-1] + C) % N] += 1
		hand -= 1

print(' '.join(map(str, A)))
