from sortedcontainers import SortedList
from bisect import insort

X = int(input())
Q = int(input())

kokuban = SortedList()
kokuban.add(X)

for _ in range(Q):
    A, B = map(int, input().split())
    kokuban.add(A)
    kokuban.add(B)
    print(kokuban[len(kokuban) // 2])
