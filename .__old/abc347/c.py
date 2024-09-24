N, A, B = map(int, input().split())
D = list(map(int, input().split()))
L = A + B
minimum, maximum = 10**9, 0
for d in D:
	m = (d % L) + 1
	minimum = min(minimum, m)
	maximum = max(maximum, m)
	
if maximum - minimum < A:
	print("Yes")
else:
	print("No")