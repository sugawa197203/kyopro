N = int(input())
import math

def A002113(n):
	if n < 2: return 0
	P = 10**math.floor(math.log10(n//2)); M = 11*P
	s = str(n - (P if n < M else M-P))
	return int(s + s[-2 if n < M else -1::-1])

print(A002113(N))