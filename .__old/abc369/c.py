N = int(input())
A = list(map(int, input().split()))
if N == 1:
    print(1)
    exit()
diff = A[1] - A[0]
ans = 1
count = 1

for i in range(1, N):
    if A[i - 1] + diff != A[i]:
        ans += (count * (count + 1)) // 2 - 1
        diff = A[i] - A[i - 1]
        count = 1
    count += 1

ans += (count * (count + 1)) // 2 - 1
print(ans)