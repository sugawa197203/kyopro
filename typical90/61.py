from collections import deque

yama = deque()

for _ in range(int(input())):
    t, x = map(int, input().split())
    if t == 1:
        yama.appendleft(x)
    elif t == 2:
        yama.append(x)
    else:
        print(yama[x-1])

