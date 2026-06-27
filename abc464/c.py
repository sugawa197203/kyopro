from collections import deque, defaultdict

N, M = map(int, input().split())

events = []
for i in range(N):
    a, d, b = map(int, input().split())
    events.append((d, i, a, b))

events.sort(key=lambda x: x[0])

events = deque(events)
colors = [-1] * N

for e in events:
    d, i, a, b = e
    colors[i] = a

count = defaultdict(int)
for color in colors:
    count[color] += 1

for day in range(1, M + 1):
    while events and events[0][0] == day:
        d, i, a, b = events.popleft()
        count[colors[i]] -= 1
        if count[colors[i]] == 0:
            del count[colors[i]]
        colors[i] = b
        count[b] += 1

    print(len(count))

