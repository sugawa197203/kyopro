H, W = map(int, input().split())
alp = ".ABCDEFGHIJKLMNOPQRSTUVWXYZ"
A = [list(map(int, input().split())) for _ in range(H)]

for _a in A:
	for a in _a:
		print(alp[a], end="")
	print()
