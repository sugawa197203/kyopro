N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

A1count = A1[0]
A2count = sum(A2)

ans = A1count + A2count
for i in range(1, N):
    A1count += A1[i]
    A2count -= A2[i - 1]
    ans = max(ans, A1count + A2count)

print(ans)

