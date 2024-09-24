N, M, K = map(int, input().split())

nm = N * M


count = (M - 1 + N - 1)

modk = ((K-1) % count) + 1
k = (K-1) // count

sumk = nm * k

_n, _m = N, M

s = 0
for _ in range(modk):
	if _m > _n:
		s = _n
		_n += N
	else:
		s = _m
		_m += M

print(sumk + s)