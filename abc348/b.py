N = int(input())
X, Y = [], []
for _ in range(N):
	x, y = map(int, input().split())
	X.append(x)
	Y.append(y)

maximum = 0
maxindex = 0
for i in range(N):
	for j in range(N):
		if i == j:
			continue
		if maximum < (maximum := max(maximum, (X[i]-X[j])**2 + (Y[i]-Y[j])**2)):
			maxindex = j
	print(maxindex+1)
	maximum	= 0
	maxindex = 0