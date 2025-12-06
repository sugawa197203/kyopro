N = int(input())
A = list(map(int, input().split()))
ans = 0
for l in range(N):
    for r in range(l, N):
        sub = A[l : r + 1]
        sumsub = sum(sub)
        if all(sumsub % x != 0 for x in sub):
            ans += 1

print(ans)