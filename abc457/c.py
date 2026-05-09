N, K = map(int, input().split())
LA = []
for _ in range(N):
    _, *A = map(int, input().split())
    LA.append(A)
C = list(map(int, input().split()))

B = []

for i, c in enumerate(C):
    B.append((c, LA[i]))

k = 0
K -= 1
# print(B)
for c, a in B:
    _k = k
    k += len(a) * c
    # print(f"{k=} {_k=}, {len(a)=}, {c=}, {a=}")
    if K < k:
        dk = (K - _k) % len(a)
        # print(f"{a=}, {dk=}, {K=}, {_k=}, {k=}, {K=}")
        print(a[dk])
        break

