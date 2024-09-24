N  = int(input())
l, r = -1, -1

ans = 0
for i in range(N):
    a, s = input().split()
    a = int(a)
    if s == "L":
        if l == -1:
            l = a
            continue
        ans += abs(a - l)
        l = a
    else:
        if r == -1:
            r = a
            continue
        ans += abs(a - r)
        r = a

print(ans)