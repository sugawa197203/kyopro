MOD = 998244353
MAX = 70
FAC = [0] * (MAX + 1)
FINV = [0] * (MAX + 1)
INV = [0] * (MAX + 1)

def init():
	FAC[0] = 1
	FAC[1] = 1
	FINV[0] = 1
	FINV[1] = 1
	for i in range(2, MAX + 1):
		FAC[i] = (FAC[i - 1] * i) % MOD
		FINV[i] = MOD - INV[MOD % i] * (MOD // i) % MOD
		FINV[i] = (FINV[i - 1] * FINV[i]) % MOD

init()

def com(n:int, k:int) -> int:
	if n < k:
		return 0
	if (n < 0) or (k < 0):
		return 0
	return (FAC[n] * (FINV[k] * FINV[n - k]) % MOD) % MOD

def NK(n:int, k:int) -> int:
	if n <= 2:
		if k == 1:
			return 1
		else:
			return 0
	if n == 3:
		if k == 1:
			return 2
		elif k == 2:
			return 1
		else:
			return 0
	ans = 0
	if k == 1:
		ans = 2
	elif k == 2:
		ans = 1
	
	_k = 4
	c = 3
	while _k <= n:
		ans += com(c, k)
		ans %= MOD
		_k <<= 1
		c += 1
	return ans

T = int(input())
for _ in range(T):
	N, K = map(int, input().split())
	
	if N <= 2:
		if K == 1:
			print(1)
		else:
			print(0)
	if N == 3:
		if K == 1:
			print(2)
		elif K == 2:
			print(1)
		else:
			print(0)
	if N >= 4:
		ans = NK(N, K)
		print(ans)
	


