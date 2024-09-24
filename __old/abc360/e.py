MOD = 998244353
N, K = map(int, input().split())

kitaiti = 0
for i in range(K):
	kuroidou = ((2 * pow(N, -1, MOD) % MOD) * pow(N - 1, i, MOD)) % MOD

