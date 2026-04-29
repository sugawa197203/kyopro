N = int(input())
A = list(map(int, input().split()))

length = A[0] - 1
count = 1

for i in range(1, N):
    if length > 0:
        length = max(length - 1, A[i] - 1)
        count += 1
    else:
        break

print(count)
