N_str = input()
N = int(N_str)

import math

def ispalindrome(n:int):
	n_str = str(n)
	for i in range(math.floor(len(n_str) / 2)):
		if n_str[i] != n_str[len(n_str) - i - 1]:
			return False
	return True

for i in range(1000000, 0, -1):
	n = i ** 3
	if ispalindrome(n) and n <= N:
		print(n)
		break
