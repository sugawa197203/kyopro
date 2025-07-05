from itertools import pairwise
from collections import Counter

T = int(input())
MOD = 10**9 + 7

def ok(n, a):
	for x, y in pairwise(range(n)):
		if (a[x] < 0 and a[y] < 0) or (a[x] > 0 and a[y] > 0):
			return False
	return True

def abssame(a):
	for x, y in pairwise(range(len(a))):
		if abs(a[x]) != abs(a[y]):
			return False
	return True

def same(a):
	for x, y in pairwise(range(len(a))):
		if a[x] != a[y]:
			return False
	return True

for _ in range(T):
	N = int(input()) # 1<N
	A = list(map(int, input().split()))
	if N == 2:
		print("Yes")
		continue

	# r = 1
	if same(A):
		print("Yes")
		continue

	# r = -1
	if abssame(A):
		c = list(Counter(A).values())
		if abs(c[0] - c[1]) < 2:
			print("Yes")
		continue
	
	# 0 < r
	A.sort(key=abs)
	for i in range(1, N - 1):
		if A[i+1] * A[i - 1] != A[i] * A[i]:
			print("No")
			break
	else:
		print("Yes")

