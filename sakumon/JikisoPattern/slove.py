N, M = map(int, input().split())
MOD = 998244353
invM = pow(M, -1, MOD)
print(invM)
# print((pow(2, N, MOD) + pow(2, N//M, MOD)*(M-1))//M % MOD)
print(((pow(2, N, MOD) + pow((M - 1) * 2, N * invM, MOD)) * invM) % MOD)
# print((2**N+2**(N//M)*(M-1))//M)
