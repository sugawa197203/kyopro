S = input()

ans = 0
for step in range(1, len(S) // 2 + 1):
	# print("step", step)
	for start in range(len(S) - step * 2):
		# print(start, step, S[start], S[start + step], S[start + step * 2])
		if S[start] == "A" and S[start + step] == "B" and S[start + step * 2] == "C":
			ans += 1

print(ans)