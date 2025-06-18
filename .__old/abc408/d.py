from itertools import groupby
from collections import deque

def A069010(n):
    return sum(1 for d in bin(n)[2:].split('0') if len(d))

T = int(input())
for _ in range(T):
	N = int(input())
	S = int(input())
	print(A069010(S) - 1)
	