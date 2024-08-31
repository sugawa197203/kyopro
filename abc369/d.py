N = int(input())
A = list(map(int, input().split()))

if N == 1:
    print(A[0])
    exit()

ans = 0

skip = False
count = 1

for i in range(2, N):
    if skip:
        skip = False
        continue
    if count % 2 == 0:
        ans += A[i - 2] * 2
        print("1", count, i, A[i - 2] * 2)
        count += 1
        continue
    if count % 2 == 1:
        a = A[i - 2] + A[i - 1] * 2 + A[i]
        b = A[i - 1] + A[i] * 2
        c = A[i - 2] + A[i] * 2
        if a >= b and a >= c:
            ans += A[i - 2]
            print("2", count, i, A[i - 2], " --- ", a, b, c)
            count += 1
        elif b >= a and b >= c:
            ans += A[i - 1]
            print("3", count, i, A[i - 1]," --- ", a, b, c)
            count += 1
            skip = True
        else:
            ans += A[i - 2]
            print("4", count, i, A[i - 2]," --- ", a, b, c)
            count += 1
            skip = True

print(count, skip, ans)

if count % 2 == 0:
    if skip:
        ans += A[N - 1] * 2
    else:
        ans += A[N - 1] * 2 + A[N - 2]
else:
    if skip:
        ans += A[N - 1] * 2
    else:
        ans += A[N - 1] * 2 + A[N - 2]

print(ans)