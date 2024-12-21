import sys
debug = lambda *args: print(*args, file=sys.stderr)
# debug = lambda *args: None
import itertools

t = list("ABCDE")
_score = map(int, input().split())
score = {}
for _t, _s in zip(t, _score):
	score[_t] = _s

ans = []
for i in range(1, 6):
	for s in itertools.combinations(t, i):
		key = "".join(s)
		_ans = 0
		for _s in s:
			_ans += score[_s]
		ans.append((key, _ans))

ans.sort(key=lambda x: x[0])
ans.sort(key=lambda x: x[1], reverse=True)

for a in ans:
	print(a[0])
		
