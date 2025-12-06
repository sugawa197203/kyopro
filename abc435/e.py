from atcoder.lazysegtree import LazySegTree
from copy import deepcopy
from bisect import bisect_left, bisect_right

N, Q = map(int, input().split())

pos = {1, N + 1}

LR = []
for _ in range(Q):
    l, r = map(int, input().split())
    LR.append((l, r))
    pos.add(l)
    pos.add(r)
    if r < N:
        pos.add(r + 1)

pos = sorted(pos)
betweenlength = []
for i in range(len(pos) - 1):
    betweenlength.append(pos[i + 1] - pos[i])

brackcount = deepcopy(betweenlength)

compressed_masu = [0] * (len(pos) - 1)

lsegtree = LazySegTree(
    op=lambda x, y: x + y,
    mapping=lambda f, x: brackcount[x] if f != -1 else x,
    composition=lambda f, g: f if f != -1 else g,
    e=0,
    id_=-1,
    v=compressed_masu)

print(pos)

for l, r in LR:
    print("-"*20)
    lidx = bisect_left(pos, l)
    ridx = bisect_left(pos, r + 1)
    lsegtree.apply(lidx, ridx, 1)
    print(lsegtree.all_prod())
    print(f"lidx: {lidx}, ridx: {ridx} for l: {l}, r: {r + 1}")
    print(f"betweenlength: {betweenlength}")
    print(f"brackcount: {brackcount}")
    print(f"masu: {[lsegtree.get(i) for i in range(len(pos)-1)]}")
