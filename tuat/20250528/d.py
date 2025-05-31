from sortedcontainers import SortedList

dict = {}

N, M = map(int, input().split())
for i, m in enumerate(range(M)):
    p, y = map(int, input().split())
    if p not in dict:
        dict[p] = SortedList()
    dict[p].add((y, i + 1))
