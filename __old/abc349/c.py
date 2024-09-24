S = list(input())
T = list(input().lower())
i = 0

for c in S:
	if c == T[i]:
		i += 1
		if i == 3:
			break
		
if i == 3:
	print("Yes")
elif i == 2 and T[2] == "x":
	print("Yes")
else:
	print("No")