s1, s2 = list(input())
t1, t2 = list(input())

def l(a, b):
	if a == "A":
		if b == "E" or b == "B":
			return 1
		else:
			return 2
	elif a == "B":
		if b == "A" or b == "C":
			return 1
		else:
			return 2
	elif a == "C":
		if b == "B" or b == "D":
			return 1
		else:
			return 2
	elif a == "D":
		if b == "C" or b == "E":
			return 1
		else:
			return 2
	else:
		if b == "D" or b == "A":
			return 1
		else:
			return 2

if l(s1, s2) == l(t1, t2):
	print("Yes")
else:
	print("No")
