import bisect

N = int(input())
A = []
for i in range(N):
	A.append(int(input()))

A = sorted(A)

count = 0
maximum = A[-1]

for i in range(N):
	if A[i] > maximum:
		break
	for j in range(i+1):
		n = A[i] * A[j]
		if n > maximum:
			break
		# exists
		left = bisect.bisect_left(A, n)
		right = bisect.bisect_right(A, n)
		count += (right - left) * 2 if i != j else (right - left)

print(count)
