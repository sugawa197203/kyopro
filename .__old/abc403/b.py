T = list(input())
U = list(input())

for start in range(len(T) - len(U) + 1):
	for i in range(len(U)):
		if T[start + i] == U[i] or T[start + i] == "?":
			continue
		break
	else:
		print("Yes")
		exit()

print("No")