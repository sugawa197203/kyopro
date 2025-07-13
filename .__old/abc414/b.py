N = int(input())
count = 0

C, L = [], []

for i in range(N):
	c, l = input().split()
	l = int(l)
	C.append(c)
	L.append(l)

if sum(L) > 100:
	print("Too Long")
else:
	ans = ""
	for i in range(N):
		ans += str(C[i]) * L[i]

	print(ans)

