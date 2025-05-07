N, X = map(int, input().split())
A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

minimum = float('inf')

xN = [0] * N
front = 0
for i in range(N):
    front += A[i] + B[i]
    nokori = X - i - 1
    if nokori < 0:
        break
    # print(minimum, front + nokori * B[i], nokori, A[i], B[i])
    minimum = min(minimum, front + nokori * B[i])

print(minimum)
