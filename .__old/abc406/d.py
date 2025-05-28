H, W, N = map(int, input().split())
X, Y = [], []
for i in range(N):
	x, y = map(int, input().split())
	X.append(x)
	Y.append(y)

from sortedcontainers import SortedList
row = {}
col = {}
for x, y in zip(X, Y):
	if x not in row:
		row[x] = SortedList()
	if y not in col:
		col[y] = SortedList()
	row[x].add(y)
	col[y].add(x)

Q = int(input())
for i in range(Q):
	q1, q2 = map(int, input().split())
	if q1 == 1:
		if q2 in row:
			print(len(row[q2]))
			xl = row[q2]
			for y in xl:
				col[y].discard(q2)
			del row[q2]
		else:
			print(0)
	elif q1 == 2:
		if q2 in col:
			print(len(col[q2]))
			yl = col[q2]
			for x in yl:
				row[x].discard(q2)
			del col[q2]
		else:
			print(0)