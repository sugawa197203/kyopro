S, T = input().split()

ans = ""
for size in range(1, len(S)):
	for j in range(1, size+1):
		i = j - 1
		ans = ""
		while i < len(S):
			ans += S[i]
			i += size
		if ans == T:
			print("Yes")
			exit()

print("No")
	