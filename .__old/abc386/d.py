N, M = map(int, input().split())
import sortedcontainers
y = N
x = sortedcontainers.SortedSet()
from collections import defaultdict

Blackd = defaultdict(int)
Whited = defaultdict(int)

for i in range(M):
	Y, X, C = input().split()
	X, Y = int(X), int(Y)
	x.add(X)
	if C == 'B':
		if X in Blackd:
			Blackd[X] = max(Blackd[X], Y)
		else:
			Blackd[X] = Y
	else:
		if X in Whited:
			Whited[X] = min(Whited[X], Y)
		else:
			Whited[X] = Y

for i in x:
	if not i in Blackd:
		if not i in Whited:
			continue
		y = Whited[i]-1
	elif not i in Whited:
		if y < Blackd[i]:
			print("No")
			exit()
	else:
		if Whited[i] < Blackd[i] or y < Blackd[i]:
			print("No")
			exit()
		y = Whited[i]-1

print("Yes")


