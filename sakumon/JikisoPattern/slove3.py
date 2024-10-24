MOD = 998244353

def mod_pow(base, exp, mod):
    """base^exp % mod を繰り返し二乗法で計算する"""
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def solve(N, M):
    # 全ての部分集合の数: 2^N % MOD
    total_subsets = mod_pow(2, N, MOD)

    # 条件を満たす部分集合の数: total_subsets / M % MOD
    M_inv = mod_pow(M, MOD - 2, MOD)  # Mの逆元 (フェルマーの小定理)
    result = (total_subsets * M_inv) % MOD

    print(result - 1)  # 空集合を除く

# 入力の読み込み
N, M = map(int, input().split())
solve(N, M)
