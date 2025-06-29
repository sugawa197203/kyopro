from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
A.sort()

for q in range(Q):
    b = int(input())
    idx = bisect_left(A, b)
    if idx == 0:
        print(abs(A[0] - b))
        continue
    if idx == N:
        print(abs(A[-1] - b))
        continue
    print(min(A[idx] - b, b - A[idx-1]))

