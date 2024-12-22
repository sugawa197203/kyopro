A, B, C = map(int, input().split())

if (A + B) == C or (A + C) == B or (B + C) == A:
	print("Yes")
elif A == B == C:
	print("Yes")
else:
	print("No")