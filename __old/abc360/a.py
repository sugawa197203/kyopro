S = list(input())

f = False

for s in S:
	if s == 'R':
		if not f:
			print("Yes")
			exit()
		else:
			print("No")
			exit()
	elif s == 'M':
		f = True