A, B = map(int, input().split())

for i in range(9):
	if not A + B == i:
		print(i)
		break