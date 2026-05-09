from math import ceil

N, K = map(int, input().split())
A = list(map(int, input().split()))

def y(A, i, x):
    a = A[i]
    # print(f"{i=}, {x=}, {a=}")
    return a + (i + 1) * x

def x(A, i, y):
    a = A[i]
    # print(f"{i=}, {y=}, {a=}")
    return (y - a + i) // (i + 1)

left = 0
right = 10**25

while left <= right:
    mid = (left + right) // 2
    xs = [max(0, x(A, i, mid)) for i in range(N)]
    sum_xs = sum(xs)
    # print(f"{left=}, {right=}, {mid=}, {xs=}, {sum_xs=}")
    if sum_xs > K:
        right = mid - 1
    else:
        left = mid + 1

# print("---" * 10)
# print(f"{left=}, {right=}, {mid=}, {xs=}")

print(left - 1)
