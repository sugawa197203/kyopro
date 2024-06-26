S = list(input())

bidxs = [i for i, s in enumerate(S) if s == 'B']

x, y = bidxs[0], bidxs[-1]
if x % 2 == y % 2:
	print("No")
	exit()
a = 0
for i, s in enumerate(S):
	if a == 0:
		if s == 'R':
			a += 1
		elif s == 'K':
			print("No")
			exit()
	elif a == 1:
		if s == 'K':
			a += 1
		elif s == 'R':
			print("No")
			exit()
	elif a == 2:
		if s == 'R':
			print("Yes")
			exit()
		elif s == 'K':
			print("No")
			exit()