N = int(input())
A = list(map(int, input().split()))
count = 0
while True:
    if sum([a > 0 for a in A]) <= 1:
        print(count)
        break
    A.sort(reverse=True)
    A[0] -= 1
    A[1] -= 1
    count += 1
