s = input()

MOD = 998244353
n = int(s)
_n = n % MOD
_n *= n
print(_n % MOD)