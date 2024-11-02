N = int(input())

import sys
debug = lambda *x: print(*x, file=sys.stderr)
dic = {}
for i in range(1, N+1):
	_q, _r = map(int, input().split())
	dic[i] = (_q, _r)

Q = int(input())
for _ in range(Q):
	a, b = map(int, input().split())
	q, r = dic[a]
	if b <= r:
		print(r)
		continue
	b -= r
	
	shou, amari = divmod(b, q)
	if amari == 0:
		print(r + b)
		continue

	print(r + q * (shou + 1))
