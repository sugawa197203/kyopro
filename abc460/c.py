from collections import deque

N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = [a * 2 for a in A]

A.sort()
B.sort()

A = deque(A)
B = deque(B)

ans = 0

while A and B:
    # no
    if A[0] < B[0]:
        A.popleft()
        continue
    ans += 1
    A.popleft()
    B.popleft()

print(ans)
