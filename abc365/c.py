N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = 0

for i in range(N):
    ans += A[i]
    if ans + A[i] * (N - i - 1) > M:
        ans -= A[i]
        print((M - ans) // (N - i))
        exit()

print("infinite")