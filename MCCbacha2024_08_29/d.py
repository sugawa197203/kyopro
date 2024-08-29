import math
N, M = map(int, input().split())
if M == 0:
    print(1)
    exit()
A = list(map(int, input().split()))
A.sort()

__A = A.copy()
if A[-1] != N:
    __A.append(N+1)

hankosize = N
before = 0
for a in __A:
    if a - before == 1:
        before = a
        continue
    hankosize = min(hankosize, a - before)
    before = a

hankosize -= 1
stampcount = 0
pos = 1
if hankosize == 0:
    print(0)
    exit()
for a in A:
    stampcount += math.ceil((a - pos) / hankosize)
    pos = a + 1

stampcount += math.ceil((N + 1 - pos) / hankosize)

print(stampcount)

