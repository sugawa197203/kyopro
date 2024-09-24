N, M = map(int, input().split(" "))

S = []

for i in range(N):
    S.append(input())

for y in range(N - 8):
	for x in range(M - 8):
		#print("1DEBUG",y, x)
		flag = False

		for i in range(3):
			for j in range(3):
				if S[y + i][x + j] != "#":
					flag = True
					break
		
		if flag:
			continue
		#print("2DEBUG",y, x)

		for i in range(3):
			for j in range(3):
				if S[y + i + 6][x + j + 6] != "#":
					flag = True
					break

		if flag:
			continue
		#print("3DEBUG",y, x)

		for i in range(4):
			if S[y + i][x + 3] != ".":
				flag = True
				break
			if S[y + i + 5][x + 5] != ".":
				flag = True
				break

		if flag:
			continue
		#print("4DEBUG",y, x)

		for i in range(3):
			if S[y + 3][x + i] != ".":
				flag = True
				break
			if S[y + 5][x + 6 + i] != ".":
				flag = True
				break

		if flag:
			continue
		#print("5DEBUG",y, x)

		print(y+1, x+1)	
		

