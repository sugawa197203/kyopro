import sys
debug = lambda *x: print(*x, file=sys.stderr)

N = int(input())
S = input()

length = 0
if "/" in S:
	length = 1
else:
	print(0)
	sys.exit()

oneCount = 0
twoCount = 0
slash = False

for s in S:
	if not slash:
		if not s == "1" and not s == "/":
			oneCount = 0
		elif s == "/":
			slash = True
		else:
			oneCount += 1
	else:
		if s == "1":
			length = max(length, min(oneCount, twoCount)*2+1)
			oneCount = 1
			twoCount = 0
			slash = False
		elif not s == "2":
			length = max(length, min(oneCount, twoCount)*2+1)
			oneCount = 0
			twoCount = 0
			slash = False
		else:
			twoCount += 1

length = max(length, min(oneCount, twoCount)*2+1)

print(length)