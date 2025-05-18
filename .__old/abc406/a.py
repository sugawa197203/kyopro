A, B, C, D = map(int, input().split())

if C < A:
	print("Yes")
elif C == A:
	if D < B:
		print("Yes")
	else:
		print("No")
else:
	print("No")