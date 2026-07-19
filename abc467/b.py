N = int(input())
loss, get = 0, 0
X = 10000
Y = 10000
for _ in range(N):
    A, B, S = input().split()
    A, B = int(A), int(B)
    X -= A
    Y -= A
    Y += A - B
    if S == "keep":
        loss += A - B
    else:
        X += A - B
        get += A - B

    # print(f"{loss=}, {get=} {X=}, {Y=}")

print(abs(Y - X))
