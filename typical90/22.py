from math import gcd

A, B, C = map(int, input().split())
size = gcd(A, gcd(B, C))
ans = A // size + B // size + C // size - 3
print(ans)

