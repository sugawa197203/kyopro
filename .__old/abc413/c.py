from collections import deque

Q = int(input())

A = deque()

for _ in range(Q):
	q, *cx = map(int, input().split())
	if q == 1:
		c, x = cx
		A.append((c, x))
	elif q == 2:
		k = cx[0]
		printval = 0
		while k > 0:
			c, x = A.popleft()
			if c <= k:
				printval += x * c
				k -= c
			else:
				printval += x * k
				A.appendleft((c - k, x))
				k = 0
		print(printval)
