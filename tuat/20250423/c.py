from sortedcontainers import SortedDict
N, M = map(int, input().split())
A = list(map(int, input().split()))
if min(A) != 0:
    print(0)
    exit()
counter = SortedDict()

for a in A[:M]:
    if a not in counter:
        counter[a] = 0
    counter[a] += 1

low, top = counter.peekitem(1)[0], 0
before = counter.peekitem(0)[0]
