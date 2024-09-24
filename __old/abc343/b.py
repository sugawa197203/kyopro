N = int(input())
A = []
for i in range(N):
	A.append(list(map(int, input().split())))

for i in range(N):
	for j in range(N):
		if A[i][j] == 1:
			print(j+1, end=' ')
	print()