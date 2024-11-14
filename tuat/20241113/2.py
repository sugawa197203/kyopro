N = int(input())
A = list(map(int, input().split()))

ans = 0
skip = False
for i in range(1, N):
    if skip:
        skip = False
        continue
    if A[i] == A[i - 1]:
        ans += 1
        skip = True

print(ans)