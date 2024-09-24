input()
P = list(map(int, input().split(" ")))
if len(P) == 1:
	print(0)
	exit()
m = max(P[1:])

d = m - P[0] + 1
if d < 0:
    print(0)
else:
    print(d)