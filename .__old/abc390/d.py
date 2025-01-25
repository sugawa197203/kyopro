N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict, Counter
import itertools

count = defaultdict(int)

s = 0
for product in itertools.product(list(range(N)), repeat=N):
	c = Counter(product)
	__f = False
	for k, _c in c.items():
		if k == 0:
			continue
		if _c == 1:
			__f = True
	
	if __f:
		continue

	a = [0] * N
	for i, p in enumerate(product):
		if p == 0:
			a[0] ^= A[i]
		else:
			a[p] += A[i]
	
	for i in range(1, N):
		a[0] ^= a[i]

	count[a[0]] += 1

print(len(count))