N, X, Y, Z = map(int, input().split())
for i in range(X, Y, 1 if X < Y else -1):
	if i == Z:
		print("Yes")
		exit()
print("No")
