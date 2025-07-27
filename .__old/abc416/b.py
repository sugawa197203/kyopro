S = input()

ans = ""
index = 0
f = True
while index < len(S):
	if S[index] == "#":
		ans += "#"
		index += 1
		f = True
		continue

	if f:
		ans += "o"
		index += 1
		f = False
	else:
		ans += "."
		index += 1

print(ans)
