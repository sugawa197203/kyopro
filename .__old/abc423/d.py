from heapq import heappop, heappush
from collections import deque

events = []

N, K = map(int, input().split())

ABC = [tuple(map(int, input().split())) for _ in range(N)]

for a, b, c in ABC:
    heappush(events, (a, 1, b, c))

k = 0
waiting = deque()

while events:
    t, e, *arg = heappop(events)

    if e == 1:
        b, c = arg
        if len(waiting) == 0 and k + c <= K:                
                heappush(events, (t + b, 2, c))
                k += c
                print(t)
        else:
            waiting.append((b, c))
    elif e == 2:
        c, = arg
        k -= c
        while waiting and k + waiting[0][1] <= K:
            b, c = waiting.popleft()
            heappush(events, (t + b, 2, c))
            k += c
            print(t)

