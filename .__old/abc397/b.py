S = input()

ans = 0

f = False
for i, s in enumerate(S):
	if not f:
		if i % 2 == 0:
			if s == "i":
				continue
			else:
				f = True
				ans += 1
		else:
			if s == "o":
				continue
			else:
				f = True
				ans += 1
	else:
		if i % 2 == 0:
			if s == "o":
				continue
			else:
				f = False
				ans += 1
		else:
			if s == "i":
				continue
			else:
				f = False
				ans += 1
if s[-1] == "i":
	ans += 1
print(ans)
