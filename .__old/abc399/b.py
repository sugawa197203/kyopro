N = int(input())
P = list(map(int, input().split()))

rank = 1

from collections import Counter, defaultdict

c = dict(Counter(P))

c = sorted(c.items(), key=lambda x: x[0], reverse=True)

c = dict(c)

ans = [0] * N

_c = defaultdict(list)

for i, p in enumerate(P):
	_c[p].append(i)
	
for __ck, __cv in c.items():
	for cc in _c[__ck]:
		ans[cc] = rank

	rank += __cv

print("\n".join(map(str, ans)))
