from collections import deque

N = int(input())
S = input()

q = deque()
f = False

for k, ch in enumerate(S, start=1):
    if ch == 'x':
        if not f:
            q.append(k)
        else:
            q.appendleft(k)
    else:
        f = not f
        if not f:
            q.appendleft(k)
        else:
            q.append(k)

if f:
    q.reverse()


print(*q)
