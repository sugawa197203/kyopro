S = input()
upperCount, lowercount = 0, 0
for s in S:
	if s.isupper():
		upperCount += 1
	else:
		lowercount += 1

if upperCount > lowercount:
	print(S.upper())
else:
	print(S.lower())