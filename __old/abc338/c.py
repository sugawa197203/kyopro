N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Acount, Bcount = 0, 0

r = N[0]

for i in range(N):
	for j in range(r):
		if A[i] * j + N[i] * j > Q[i]:
			break
		

