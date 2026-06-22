from math import sqrt

N = int(input())
A = list(map(int, input().split()))
hako = []

for i in range(N, 0, -1):
    if i > sqrt(N):
        hako.append(A[i - 1])
        print(A[i - 1])
        continue

    _sum = sum(a for k, a in enumerate(A, 1) if i % k == 0)
    print(f"i: {i}, sum: {_sum}, A[i-1]: {A[i - 1]}")
    if _sum % 2 == A[i - 1]:
        hako.append(1)
    else:
        hako.append(0)

hako.reverse()
ans = []
for i in range(1, N + 1):
    if hako[i - 1] == 1:
        ans.append(i)
print(hako)
print(len(ans))
print(*ans)
