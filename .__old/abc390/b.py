N = int(input())
A = list(map(int, input().split()))

start = A[0]
r = A[1] / start

if N == 2:
	print("Yes")
	exit()

before = A[1]
for i in range(2, N):
	if before * r != A[i]:
		print("No")
		exit()
	before = A[i]

print("Yes")