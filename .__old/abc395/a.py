N = int(input())
A = list(map(int, input().split()))

b = A[0]

for a in A[1:]:
	if a <= b:
		print('No')
		exit()
	b = a

print('Yes')