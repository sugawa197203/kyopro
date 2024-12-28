S = list(input())

ans = 0

f = False
for i, s in enumerate(S):
	if f:
		f = False
		continue
	if s != "0":
		ans += 1
	elif s == "0" and i < len(S) - 1 and S[i + 1] == "0":
		ans += 1
		f = True
	else:
		ans += 1

print(ans)