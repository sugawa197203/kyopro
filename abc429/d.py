from collections import Counter, defaultdict
from bisect import bisect_right

N, M, C = map(int, input().split())
AA = list(map(int, input().split()))
Ac = sorted(Counter(AA).items(), key=lambda x: x[0])

acc = {}

if Ac[0][0] == 0:
    acc[0] = Ac[0][1]
else:
    acc[0] = 0

for ac in Ac:
    acc[ac[0]] = acc[ac[0] - 1] + ac[1]

acckey = list(acc.keys())

ans = 0
print(acc)
print(acckey)
def getAcc(i):
    if i in acc:
        return acc[i]
    else:
        idx = bisect_right(acckey, i)
        if idx == 0:
            return 0
        else:
            return acc[acckey[idx - 1]]

searchM = dict()
searchM[0] = 1

for i in range(len(acckey)):
    ack = acckey[i]
    _ack = 0 if i == 0 else acckey[i - 1]
    searchM[ack] = ack - _ack

if M - 1 not in searchM:
    searchM[M - 1] = M - 1 - acckey[-1]

print(f"{searchM=}")

for km, vm in searchM.items():
    left = -1
    right = M - 1
    val = 0
    while right - left > 1:
        mid = (left + right) // 2
        val = 0
        if mid + km < M:
            val += getAcc(mid + km) - getAcc(km)
        else:
            val += getAcc(M - 1) - getAcc(km) + getAcc((mid + km) % M)
            # print(">", getAcc(M - 1) - getAcc(km) + getAcc((mid + km) % M), val)

        if val <= C:
            left = mid
        else:
            right = mid

    v = 0
    if right + km < M:
        v += getAcc(right + km) - getAcc(km)
    else:
        # print(f">> {getAcc(M - 1) - getAcc(m)} + {getAcc((right + m) % M)}")
        v += getAcc(M - 1) - getAcc(km) + getAcc((right + km) % M)
    # print(f"m={m}, right={right}, v={v}")
    ans += v * vm
    # print("---")

print(ans)
