T, S = map(int, input().split())
T = list(map(int, input().split()))

TT = 0

for t in T:
	if t - TT > S:
		print("No")
		exit()
	TT = t

print("Yes")