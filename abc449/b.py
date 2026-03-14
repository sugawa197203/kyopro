H, W, Q = map(int, input().split())

for _ in range(Q):
    q, RC = map(int, input().split())
    if q == 1:
        print(RC * W)
        H -= RC
    else:
        print(RC * H)
        W -= RC
