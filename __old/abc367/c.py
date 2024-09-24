N, K = map(int, input().split())
R = list(map(int, input().split()))

ans = [1] * N

while True:
    sm = sum(ans)
    if sm % K == 0:
        print(" ".join(map(str, ans)))
    for i in range(N-1, -1, -1):
        ans[i] += 1
        if ans[i] <= R[i]:
            break
        ans[i] = 1

    if sum(ans) == N:
        break

