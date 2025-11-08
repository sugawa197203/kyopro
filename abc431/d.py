from collections import deque

N = int(input())
WHB = [tuple(map(int, input().split())) for _ in range(N)]

watched = {}

l = [(0, 0, 0)]

for w, h, b in WHB:
    nextl = []
    for _h, _b, u in l:
        nh, nb = _h + w, _b + w

        if (nh - _b) not in watched:
            watched[(nh - _b)] = u + h
            nextl.append((nh, _b, u + h))
        elif watched[(nh - _b)] < u + h:
            watched[(nh - _b)] = u + h
            nextl.append((nh, _b, u + h))

        if (_h - nb) not in watched:
            watched[(_h - nb)] = u + b
            nextl.append((_h, nb, u + b))
        elif watched[(_h - nb)] < u + b:
            watched[(_h - nb)] = u + b
            nextl.append((_h, nb, u + b))

    l = nextl
    # print("-" * 20)
    # print(l)
    # print(watched)


print(max(u for h, b, u in l if h <= b))

