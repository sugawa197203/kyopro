import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))
Aref = list(range(N))

for _ in range(Q):
	t, x, y = map(int, input().split())
	if t == 1:
		A[x-1] = y
	elif t == 2:
		if y - x < 2:
			print('0')
			continue
		Aref = Aref[:x-1] + sorted(Aref[x-1:y], key=lambda i: A[i]) + Aref[y:]
		maximum = A[Aref[x-1:y][-1]]
		maxleft = bisect.bisect_left(Aref[x-1:y], maximum, key=lambda i: A[i]) - x + 1
		if maxleft == 0:
			print('0')
		else:
			nextMax = A[Aref[x-1:y][maxleft-1]]
			right = bisect.bisect_right(Aref[x-1:y], nextMax, key=lambda i: A[i])
			left = bisect.bisect_left(Aref[x-1:y], nextMax, key=lambda i: A[i])
			print(right - left)
