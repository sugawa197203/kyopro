N, Q = map(int, input().split())
ans = 0
R, L = 2, 1
for i in range(Q):
	H, T = input().split()
	T = int(T)
	if H == "R":
		l = 0
		r1f = r2f = False
		r1 = r2 = R
		if R == T:
			continue
		while True:
			r1 += 1
			r2 -= 1
			l += 1
			if r1 > N:
				r1 = 1
			if r2 <= 0:
				r2 += N
			if r1 == L:
				r1f = True
			if r2 == L:
				r2f = True

			if (r1 == T and not r1f) or (r2 == T and not r2f):
				break
		
		if not r1f and r1 == T:
			R = r1
		elif not r2f and r2 == T:
			R = r2
		ans += l

	else:
		l = 0
		l1f = l2f = False
		l1 = l2 = L
		if L == T:
			continue
		while True:
			l1 += 1
			l2 -= 1
			l += 1
			if l1 > N:
				l1 = 1
			if l2 <= 0:
				l2 += N
			if l1 == R:
				l1f = True
			if l2 == R:
				l2f = True
			if (l1 == T and not l1f) or (l2 == T and not l2f):
				break
		
		if not l1f and l1 == T:
			L = l1
		elif not l2f and l2 == T:
			L = l2
		ans += l
	

print(ans)
