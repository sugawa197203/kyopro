N = int(input())
S = list(input())

a, c = 0, 0
for i, s in enumerate(S):
	if s == '1':
		a += i
		c += 1

if c == 1:
	print(0)
	exit()

a /= c
ans = 0
kaburi = [0] * N
for i, s in enumerate(S):
	if s == '1':
		d = int(a - i)
		# print(i, a, d)
		kaburi[i + d] += 1
		ans += abs(d)

# print(a, kaburi)
kc = 0
for i in range(N):
	if kaburi[i] > 1:
		v = 0
		n = kaburi[i]
		_n = n // 2
		v += _n * (_n + 1)
		if n % 2 == 0:
			v -= _n
		# print(v, _n)
		kc += v
print(ans - kc)
