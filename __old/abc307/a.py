N = int(input())
A = list(map(int, input().split(' ')))

for i in range(N):
	a = A[i * 7]
	a += A[i * 7 + 1]
	a += A[i * 7 + 2]
	a += A[i * 7 + 3]
	a += A[i * 7 + 4]
	a += A[i * 7 + 5]
	a += A[i * 7 + 6]
	print(a, end=' ')
