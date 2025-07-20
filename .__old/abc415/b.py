S = list(input())

f = False

for i in range(len(S)):
	if S[i] == "#":
		if not f:
			f = True
			print(i + 1, end=",")
		else:
			print(i + 1)
			f = False

