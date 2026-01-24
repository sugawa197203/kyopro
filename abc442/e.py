from math import cos, sin, atan2

from atcoder.segtree import SegTree
from bisect import bisect_left, bisect_right
from collections import defaultdict

INF = 1 << 63
ID = INF

anglecount = defaultdict(int)

class Monster:
    def __init__(self, idx, x, y, num=1):
        self.idx = idx
        self.x = x
        self.y = y
        self.num = num
        self.angle = -atan2(y, x)
        anglecount[self.angle] += 1

def op(ele1: Monster, ele2: Monster):
    return Monster(-1, -1, -1, ele1.num + ele2.num)

e = Monster(-1, -1, -1, 0)
id_ = ID

N, Q = map(int, input().split())
XY = []
for i in range(N):
    x, y = map(int, input().split())
    XY.append(Monster(i+1, x, y))
unsortXY = XY.copy()
XY.sort(key=lambda m: m.angle)

zeroright_idx = bisect_right(XY, 0, key=lambda m: m.angle)
XY = XY[zeroright_idx:] + XY + XY[:zeroright_idx]

Angle2Idx = {}
IdxFix = [0] * N
for i in range(N):
    xy = unsortXY[i]
    if xy.angle not in Angle2Idx:
        Angle2Idx[xy.angle] = xy.idx
    else:
        Angle2Idx[xy.angle] = min(Angle2Idx[xy.angle], xy.idx)
        # xy.idx = Angle2Idx[xy.angle]

print(Angle2Idx)
for i in range(N):
    xy = XY[i]
    IdxFix[xy.idx - 1] = i if Angle2Idx[xy.angle] == xy.idx else Angle2Idx[xy.angle]

print([(xy.angle, xy.idx) for xy in XY])
print([(xy.angle, xy.idx) for xy in unsortXY])

seg = SegTree(op, e, XY)

print(IdxFix)

for _ in range(Q):
    print("-----")
    a, b = map(int, input().split())
    fixa, fixb = IdxFix[a-1], IdxFix[b-1]
    print(f"a={a}, b={b}, fixa={fixa}, fixb={fixb}")
    if fixa > fixb:
        fixb += N
    print(f"a={a}, b={b}, fixa={fixa}, fixb={fixb}")

    if fixa == fixb:
        print(anglecount[XY[fixa].angle])
    else:
        print(seg.prod(fixa, fixb + 1).num)