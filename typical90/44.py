N, Q = map(int, input().split())
A = list(map(int, input().split()))
offset = 0
for _ in range(Q):
    t, x, y = map(int, input().split())
    x -= 1
    y -= 1
    if t == 1:
        x = (x + offset) % N
        y = (y + offset) % N
        A[x], A[y] = A[y], A[x]
    elif t == 2:
        offset = (offset - 1) % N
    elif t == 3:
        print(A[(x + offset) % N])

