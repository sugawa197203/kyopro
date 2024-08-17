N, M = map(int, input().split())
A = list(map(int, input().split()))

A2 = [0] * (2 * N - 1)
A2[0] = A[0]
for i in range(1, N):
    A2[i] = A[i] % M
    A2[N + i - 1] = A[i-1] % M

ans = 0
count = 0
for i in range(N):
    count += A2[i]
    count %= M
    print(i, count)
    if count == 0:
        ans += i + 1

print(ans)
for i in range(N, 2 * N - 1):
    count += A2[i]
    count %= M
    if count == 0:
        ans += N - i

print(ans)
