import bisect

N = int(input())
S = list(input())
Q = int(input())

ALFABET = list("abcdefghijklmnopqrstuvwxyz")
CHANGE_TABLE = list("abcdefghijklmnopqrstuvwxyz")

for i in range(Q):
	# c to d
	c, d = input().split()
	CHANGE_TABLE = [d if x == c else x for x in CHANGE_TABLE]

for s in S:
	alfabetIndex = bisect.bisect_left(ALFABET, s)
	print(CHANGE_TABLE[alfabetIndex], end="")
	
