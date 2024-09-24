N, D = map(int, input().split(" "))

X, Y = [], []

for i in range(N):
	x, y = map(int, input().split(" "))
	X.append(x)
	Y.append(y)
	
v0x = X[0]
v0y = Y[0]
D = D * D

buf = []

flag = set()

for i in range(N):
	d = (v0x - X[i]) ** 2 + (v0y - Y[i]) ** 2
	if d <= D:
		buf.append(i)
		flag.add(i)

for i in buf:
	x = X[i]
	y = Y[i]
	for j in range(N):
		if j in flag or j == i:
			continue

		d = (x - X[j]) ** 2 + (y - Y[j]) ** 2

		if d <= D:
			buf.append(j)
			flag.add(j)

for i in range(N):
	if i in flag:
		print("Yes")
	else:
		print("No")
	


