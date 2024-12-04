N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

_A = []
mina, minai = 2*10**5+1, 2*10**5+1
for i, a in enumerate(A):
	if a <= mina:
		mina = a
		minai = i
	_A.append((mina, minai))

import bisect
_A = list(reversed(_A))
for b in B:
	ai = bisect.bisect_right(_A, b, key=lambda x: x[0])
	ai -= 1
	if ai < 0:
		print(-1)
	else:
		print(_A[ai][1] + 1)