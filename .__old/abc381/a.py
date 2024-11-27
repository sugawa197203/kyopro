import sys
debug = lambda *x: print(*x, file=sys.stderr)

N = int(input())
S = input()

if not len(S) % 2 == 1:
	debug(1)
	print("No")
	exit()

_s = S.split("/")

if not len(_s) == 2:
	debug(2)
	print("No")
	exit()

if not _s[0] == "1"*len(_s[0]):
	debug(3)
	print("No")
	exit()

if not _s[1] == "2"*len(_s[1]):
	debug(4)
	print("No")
	exit()

if not len(_s[0]) == len(_s[1]):
	debug(5)
	print("No")
	exit()

print("Yes")