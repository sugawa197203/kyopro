X1, X2, X3 = map(int, input().split())
sumX = X1 + X2 + X3
ans = 0

MOD = 998244353

INVFACT = [1] * (sumX + 1)
for i in range(sumX):
    INVFACT[i - 1] = INVFACT[i] * i % MOD

def comb(n, r):
    if r < 0 or r > n:
        return 0
    return INVFACT[n] * INVFACT[r] * INVFACT[n - r] % MOD

for i in range(1, min(X1, X2 + 1) + 1):
    X1_pattern = comb(X2 + 1, i) * comb(X1 - 1, i - 1) % MOD
    X3_pattern = comb(X2 + X3 - i, X2 - i) % MOD
    ans += X1_pattern * X3_pattern % MOD
    ans %= MOD

print(ans)

