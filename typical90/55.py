from itertools import combinations

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for a in combinations(A, 5):
    num = a[0] % P
    num *= a[1] % P
    num %= P
    num *= a[2] % P
    num %= P
    num *= a[3] % P
    num %= P
    num *= a[4] % P
    num %= P

    if num == Q:
        ans += 1

print(ans)

