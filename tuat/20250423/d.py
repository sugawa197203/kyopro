N, M, Q = map(int, input().split())
L, R = [], []
for _ in range(M):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
p, q = [], []
for _ in range(Q):
    p_, q_ = map(int, input().split())
    p.append(p_)
    q.append(q_)

LR1 = [(l, r) for l, r in zip(L, R)]
LR2 = LR1.copy()

LR1.sort(key=lambda x: x[0])
LR2.sort(key=lambda x: x[1])

