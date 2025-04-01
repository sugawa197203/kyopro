T = int(input())

for _ in range(T):
	N = int(input())
	A = list(map(int, input().split()))
	last = -1
	l = []
	s = set()
	for i in range(2 * N):
		if A[i] == last:
			s.remove(A[i])
			l.append(s)
			s = set()
			last = -1
		else:
			if A[i] in s:
				l.append(s)
				s = set()
				s.add(A[i])
				last = A[i]
			else:
				last = A[i]
				s.add(A[i])

	l.append(s)
	ans = sum(max(len(x) - 1, 0) for x in l)
	print(ans // 2)


