from heapq import heapify, heappush, heappop

N, K = map(int, input().split())
A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append((-a, -1))
    B.append((-b, i))

heapify(B)
ans = 0

for k in range(K):
    b, idx = heappop(B)
    ans -= b
    if idx != -1:
        heappush(B, (A[idx][0] - b, A[idx][1]))

print(ans)

