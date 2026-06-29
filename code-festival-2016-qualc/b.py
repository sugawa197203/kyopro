K, T = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)

g1, g2 = 0, 0
for a in A:
    if g1 <= g2:
        g1 += a
    else:
        g2 += a

print(max(abs(g1 - g2) - 1, 0))
