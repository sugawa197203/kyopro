from sortedcontainers import SortedList
from collections import defaultdict

N, K, M = map(int, input().split())
CV = [list(map(int, input().split())) for _ in range(N)]
CV.sort(key=lambda x: x[1],)
alls = SortedList()
ans = []
Jewels = defaultdict(list)
for c, v in CV:
    Jewels[c].append(v)
    alls.add(v)

tops = []

for k, v in Jewels.items():
    tops.append(v[-1])
    alls.remove(v[-1])
    v.pop()

tops.sort()
for t in tops[::-1]:
    ans.append(t)
    M -= 1
    K -= 1
    tops.pop()
    if M == 0 and len(tops) != 0:
        for _t in tops:
            alls.add(_t)
        break

if K != 0:
    for al in alls[::-1]:
        ans.append(al)
        K -= 1
        if K == 0:
            break

print(sum(ans))
