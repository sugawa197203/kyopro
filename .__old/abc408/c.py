N, M = map(int, input().split())
count = [0] * N

L = []
R = []

for _ in range(M):
	l, r = map(int, input().split())
	l -= 1
	r -= 1
	L.append(l)
	R.append(r)

a = 0
L.sort()
R.sort()

from collections import deque

L = deque(L)
R = deque(R)
for i in range(N):
	while L and i == L[0]:
		a += 1
		L.popleft()
	count[i] = a
a = 0
_a = 0
for i in range(N):
	while R and i == R[0]:
		_a += 1
		R.popleft()
	count[i] -= a
	a = _a

print(min(count))