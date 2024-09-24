N, K = map(int, input().split())
A = list(map(int, input().split()))

a = A[:N-K]
b = A[N-K:]

print(*(b+a))