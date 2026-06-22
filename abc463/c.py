N = int(input())
HL = [tuple(map(int, input().split())) for _ in range(N)]
Q = int(input())
T = [(t, i) for i, t in enumerate(map(int, input().split()))]
T.sort(key=lambda x: x[0])
HL.sort(key=lambda x: x[1], reverse=True)
# print(T)
# print(HL)
from bisect import bisect_right
max_h = [(0, 0)] + [(0, t) for h, t in HL]
for i in range(N):
    max_h[i + 1] = (max(max_h[i][0], HL[i][0]), max_h[i + 1][1])
max_h = max_h[1:]
max_h.sort(key=lambda x: x[1])

_filter = {}
_max_h = []
for h, t in max_h:
    if t in _filter and _filter[t] >= h:
        continue
    if t not in _filter:
        _filter[t] = h
    else:
        _filter[t] = max(_filter[t], h)
    # _max_h.append((_filter[t], t))

for t, h in _filter.items():
    _max_h.append((h, t))
_max_h.sort(key=lambda x: x[1])
max_h = _max_h

# print(f"{_filter=}")
max_h = _max_h
# print(f"{max_h=}")
ans = [(-1, i) for t, i in T]

for t, i in T:
    index = bisect_right(max_h, t, key=lambda x: x[1])
    # print(f"{t=}, {i=}, {index=}")
    ans[i] = (max_h[index][0], i)
ans.sort(key=lambda x: x[1])
# print(ans)

for a, i in ans:
    print(a)
