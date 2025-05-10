MOD = 998244353
MAX = 4 * 10**6 + 10  # A+B+C+D が最大でも400万になることを想定

# 階乗とその逆元を事前計算
fact = [1] * MAX
invfact = [1] * MAX

# 累積階乗
for i in range(1, MAX):
    fact[i] = fact[i - 1] * i % MOD

# 逆元の累積
invfact[MAX - 1] = pow(fact[MAX - 1], MOD - 2, MOD)
for i in range(MAX - 2, -1, -1):
    invfact[i] = invfact[i + 1] * (i + 1) % MOD

# 組み合わせ関数
def comb(n, k):
    if k < 0 or k > n:
        return 0
    return fact[n] * invfact[k] % MOD * invfact[n - k] % MOD

# 入力
A, B, C, D = map(int, input().split())

# 解法：A を最初に配置、その後 B+C を混ぜ、D を最後に置く
res = comb(A + B + C + D, A)
res = res * comb(B + C, B) % MOD

print(res)
