from collections import defaultdict
from math import isqrt

N = int(input())
A = list(map(int, input().split()))
A = sorted(A)

count = 0

A = sorted(A)
print(A)
def count_square_pairs(A):
	# 素因数分解の結果を保持する辞書
	factorizations = [defaultdict(int) for _ in A]

	# 各整数を素因数分解
	for i, a in enumerate(A):
		for j in range(2, isqrt(a) + 1):
			while a % j == 0:
				a //= j
				factorizations[i][j] += 1
		if a > 1:
			factorizations[i][a] += 1
			
	print(factorizations)

	# 各整数の素因数の指数が全て偶数であるかを確認
	counts = defaultdict(int)
	for factorization in factorizations:
		for factor, exponent in factorization.items():
			if exponent % 2 == 1:
				counts[factor] += 1
	print(counts)
	# 解の計算
	result = 0
	for count in counts.values():
		print(count)
		result += count * (count - 1) // 2
	return result

for a in A:
	if a == 0:
		count += len(A) - 1
	else:
		break

print(">", count_square_pairs(A) + count)
print(">", count)
