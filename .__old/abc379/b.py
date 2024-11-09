N, K = map(int, input().split())
S = input()

ans = 0

target = "O" * K

# find target in S
while True:
	idx = S.find(target)
	if idx == -1:
		print(ans)
		break
	ans += 1
	S = S[:idx] + "XXX" + S[idx + K:]
