N = int(input())
A = list(input())
B = list(input())
C = list(input())

count = 0

for i in range(N):
	if A[i] == B[i] == C[i]:
		pass
	elif A[i] == B[i] or B[i] == C[i] or C[i] == A[i]:
		count += 1
	else:
		count += 2

print(count)
