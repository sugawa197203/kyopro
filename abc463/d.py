N, K = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in range(N)]
Li = [(l, i) for i, (l, r) in enumerate(LR)]
Ri = [(r, i) for i, (l, r) in enumerate(LR)]

Li.sort(key=lambda x: x[0])
Ri.sort(key=lambda x: x[0])

from bisect import bisect_right, bisect_left
print(f"{Li=}")
print(f"{Ri=}")
NEXT = [(-1, -1)] * N

for i in range(N):
    end = Ri[i]
    index = bisect_right(Li, end[0], key=lambda x: x[0])
    print(f"{i=}, {end=}, {index=}", end="")
    if index >= len(Li):
        print("")
        continue

    length = Li[index][0] - Ri[i][0]
    print(f", {length=}, {Li[index]=}")
    NEXT[Ri[i][1]] = (length, Li[index][1])

from sortedcontainers import SortedList
from collections import deque

FLAG = [False] * N
ans = -1
print(f"{NEXT=}")
for i in range(N):
    # if FLAG[i]:
    #     continue
    if NEXT[i][0] == -1:
        continue
    FLAG[i] = True
    length_list = SortedList()
    q = deque()
    now = NEXT[i]
    minimum = 10**9
    print(f"----------")
    while now != (-1, -1):
        length_list.add(now[0])
        q.append(now[0])
        if len(length_list) > K - 1:
            length_list.remove(q.popleft())
        print(f"{now=}, {length_list=}, {q=}, {minimum=}")
        # input()
        FLAG[now[1] - 1] = True
        now = NEXT[now[1]]
        if len(length_list) == K - 1:
            minimum = min(minimum, length_list[-1])
    
    if minimum != 10**9:
        ans = max(ans, minimum)

print(ans)
