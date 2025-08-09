from math import gcd
from collections import defaultdict
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

N = int(input())
XY = [(x, y) for x, y in (map(int, input().split()) for _ in range(N))]

vectors = defaultdict(int)
heiko = defaultdict(int)

for i in range(N):
	xy = XY[i]
	for k in range(i + 1, N):
		_xy = XY[k]
		heiko[(xy[0] + _xy[0], xy[1] + _xy[1])] += 1

heikocnt = 0

for v in heiko.values():
	if v >= 2:
		heikocnt += v * (v - 1) // 2

# print(heikocnt)

for i in range(N):
	for j in range(i + 1, N):
		v = (XY[j][0] - XY[i][0], XY[j][1] - XY[i][1])
		if v[0] < 0:
			v = (-v[0], -v[1])
		if v[0] == 0 and v[1] < 0:
			v = (0, -v[1])
		
		g = gcd(v[0], v[1])
		vectors[(v[0] // g, v[1] // g)] += 1

ans = 0
for k, v in vectors.items():
	# print(k, v)
	if v >= 2:
		ans += v * (v - 1) // 2

print(ans - heikocnt)
