from atcoder.segtree import SegTree

INF = 1 << 63
ID = INF

def op(ele1, ele2):
    return ele1 + ele2

e = 0
id_ = ID

N, Q = map(int, input().split())
A = list(map(int, input().split()))

seg = SegTree(op, e, A)

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, x = query
        val_x = seg.get(x - 1)
        val_x_1 = seg.get(x)
        seg.set(x - 1, val_x_1)
        seg.set(x, val_x)
    else:
        _, l, r = query
        print(seg.prod(l - 1, r))
