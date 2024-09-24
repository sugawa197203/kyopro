import bisect

N, T = map(int, input().split())
S = list(input())
X = list(map(int, input().split()))

migi, hidari = [], []
count = 0

for s, x in zip(S, X):
	if s == '1':
		migi.append(x)
	else:
		hidari.append(x)

migi.sort()
hidari.sort()

for _migi in migi:
	start, goal = _migi, _migi + (2 * T)
	startind = bisect.bisect_left(hidari, start)
	goalind = bisect.bisect_right(hidari, goal)
	count += goalind - startind

# for _hidari in hidari:
# 	start, goal = _hidari, _hidari - (2 * T)
# 	startind = bisect.bisect_right(migi, start)
# 	goalind = bisect.bisect_left(migi, goal)
# 	count += startind - goalind

print(count)
