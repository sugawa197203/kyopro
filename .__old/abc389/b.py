X = int(input())
a = 2
while True:
	if a == X:
		print(a)
		break
	X /= a
	a += 1