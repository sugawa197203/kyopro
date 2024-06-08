N, M = map(int, input().split())
H = list(map(int, input().split()))
for i, h in enumerate(H):
	M -= h
	if M < 0:
		print(i)
		exit()

print(N)