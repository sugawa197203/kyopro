N, D = map(int, input().split())
S = input()
ans = ""

for s in reversed(S):
	if s == ".":
		ans += "."
	elif s == "@":
		if not D == 0:
			ans += "."
			D -= 1
		else:
			ans += s

print(ans[::-1])