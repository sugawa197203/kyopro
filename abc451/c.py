from sortedcontainers import SortedList

Q = int(input())

trees = SortedList()

for _ in range(Q):
    q, h = map(int, input().split())
    if q == 1:
        trees.add(h)
    else:
        idx = trees.bisect_right(h)
        for i in range(idx):
            front = trees[0]
            trees.remove(front)

    print(len(trees))
