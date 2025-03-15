N = int(input())

if N == 1:
	print("-1")
	exit()

soinsuu = []

def primeFactorize(n:int) -> list:
	res:list[tuple[int, int]] = []
	a = 2

	while a * a <= n:
		if n % a != 0:
			a += 1
			continue
		
		ex = 0
		while n % a == 0:
			ex += 1
			n //= a
		res.append((a, ex))
		a += 1
	if n != 1:
		res.append((n, 1))
	return res

print(primeFactorize(N))