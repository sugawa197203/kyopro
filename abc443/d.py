def solve(N:int, R:list[int]):
    left, right = [0] * N, [0] * N
    left[0] = R[0]
    right[N - 1] = R[N - 1]
    for i in range(1, N):
        left[i] = min(R[i], left[i-1] + 1)
    for i in range(N - 2, -1, -1):
        right[i] = min(R[i], right[i+1] + 1)
    ans = [0] * N
    for i in range(N):
        ans[i] = min(left[i], right[i])
    print("----------")
    print(f"R: {R}")
    print(f"left: {left}")
    print(f"right: {right}")
    print(f"ans: {ans}")
    print(sum(R) - sum(ans))

__T__ = int(input())
for _ in range(__T__):
    N = int(input())
    R = list(map(int, input().split()))
    solve(N, R)