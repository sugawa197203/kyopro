N = int(input())
A = list(map(int, input().split()))

length = A[0]
i = 2
    
while i <= length and i <= N:
    length = max(length, i + A[i - 1] - 1)
    i+=1

print(min(length, N))