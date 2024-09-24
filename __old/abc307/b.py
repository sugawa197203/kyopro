N = int(input())

A = []
for i in range(N):
	A.append(input())

for i in range(N):
	for j in range(N):
		if i == j:
			continue
		s1 = A[i] + A[j]
		s2 = s1[::-1]
		if s1 == s2:
			print("Yes")
			exit()

print("No")
