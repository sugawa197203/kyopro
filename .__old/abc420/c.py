N, Q = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = sum(min(A[i], B[i]) for i in range(N))

for _ in range(Q):
    c, x, v = input().split()
    x, v = int(x) - 1, int(v)

    before = min(A[x], B[x])
    if c == "A":
        A[x] = v
    else:
        B[x] = v

    after = min(A[x], B[x])
    
    if before != after:
        ans += after - before

    print(ans)