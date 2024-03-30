Q = int(input())

A = []

for i in range(Q):
	n, xk = map(int, input().split())
	if n == 1:
		A.append(xk)
	else:
		print(A[-xk])