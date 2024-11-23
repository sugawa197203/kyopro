import sys
debug = lambda *x: print(*x, file=sys.stderr)

S = list(input())
if not len(S) % 2 == 0:
	debug(1)
	print("No")
	exit()

S = list(S)

for i in range(len(S)//2):
	if not S[2*i] == S[2*i+1]:
		debug(2)
		print("No")
		exit()

d = dict()

for s in S:
	if not s in d:
		d[s] = 0
	d[s] += 1

for v in d.values():
	if not v == 2:
		debug(3)
		print("No")
		exit()

print("Yes")
