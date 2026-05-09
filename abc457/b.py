N = int(input())
LA = []
for _ in range(N):
    _, *A = map(int, input().split())
    LA.append(A)
X, Y = map(int, input().split())
print(LA[X-1][Y-1])
