N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    for j in range(i, -1, -1):
        if A[i] < A[j]:
            print(j + 1)
            break
    else:
        print("-1")

