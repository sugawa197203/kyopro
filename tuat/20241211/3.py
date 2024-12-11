N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = sum(x * (i+1) for i, x in enumerate(A[0:M]))
diff = sum(A[0:M])
total = ans
for i in range(M, N):
    new = total - diff + A[i] * M
    diff += A[i] - A[i - M]
    ans = max(ans, new)
    total = new

print(ans)