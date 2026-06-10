N, Q = map(int, input().split())

from sortedcontainers import SortedList

baseline = 0
hightByTower = [0] * N

S = SortedList([0] * N)

for _ in range(Q):
    q, v = map(int, input().split())
    if q == 1:
        x = v - 1
        before = hightByTower[x]
        S.remove(before)
        hightByTower[x] += 1
        S.add(hightByTower[x])
        index = S.bisect_right(baseline)
        if index == 0:
            baseline += 1
    else:
        y = v + baseline
        index = S.bisect_left(y)
        print(N - index)
        


