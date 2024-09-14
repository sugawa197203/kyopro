import bisect
N = int(input())
X = list(map(int, input().split()))
P = list(map(int, input().split()))
sums = []
sump = 0
for x, p in zip(X, P):
    sump += p
    sums.append((x, sump))
Q = int(input())

for i in range(Q):
    l, r = map(int, input().split())

    if N == 1:
        if l <= X[0] <= r:
            print(P[0])
        else:
            print(0)
        continue

    right = bisect.bisect_right(sums, r, key=lambda x: x[0])
    left = bisect.bisect_left(sums, l, key=lambda x: x[0])

    print(sums[right-1][1] - sums[left][1] + P[left])