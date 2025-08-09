S = list(input())
ans = 0
for length in range(3, len(S)+1):
	for start in range(len(S) - length + 1):
		ss = S[start:start + length]
		if ss[0] == ss[-1] == "t":
			tcnt = ss.count("t")
			ans = max(ans, (tcnt - 2) / (len(ss) - 2))

print(ans)
