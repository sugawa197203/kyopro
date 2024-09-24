N, T, P = map(int, input().split())
L = list(map(int, input().split()))

c = 0
while True:
	if sum([l >= T for l in L]) >= P:
		print(c)
		break

	c += 1
	L = [l+1 for l in L]