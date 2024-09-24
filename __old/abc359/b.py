N = int(input())
A = list(map(int, input().split()))

print(sum([A[i] == A[i+2] for i in range(2*N-2)]))