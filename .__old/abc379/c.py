N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

XA = list(zip(X, A))
XA.sort(key=lambda x: x[0])
X, A = zip(*XA)

import sys
# debug = lambda *a : print(*a, file=sys.stderr)
debug = lambda *a : None

ans = 0
nokori = A[0]
pos = 1

if X[0] != 1:
	debug("X[0] != 1")
	print(-1)
	exit()

if M == 1:
	if A[0] < N:
		debug("A[0] < N")
		print(-1)
		exit()
	else:
		print(A[0] * (A[0] - 1) // 2)
		debug("A[0] * (A[0] - 1) // 2")
		exit()

for x, a in zip(X[1::], A[1::]):
	diff = x - pos
	debug(f"diff={diff}, a={a}, nokori={nokori} pos={pos}")
	if diff > nokori:
		print(-1)
		exit()
	else:
		nokori -= diff
		nokori += a
		debug(f"nokori={nokori} ans={ans} pos={pos} diff={diff}")
		ans += (diff * (diff - 1)) // 2 + max(diff * (nokori - diff), 0)
		pos = x
	
	debug(f"nokori={nokori} ans={ans} pos={pos}")

if nokori <= N - pos:
	print(-1)
	exit()

ans += (N - pos) * (N - pos - 1) // 2 + max((N - pos) * (nokori - (N - pos)), 0)

print(ans)
