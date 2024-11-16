N, K = map(int, input().split())
S = list(input())

targetIndex = 0
insertIndex = 0
count = 0

oneFlag = False
for i in range(N):
	if not oneFlag and S[i] == "1":
		count += 1
		oneFlag = True
	elif oneFlag and S[i] == "0":
		oneFlag = False
		if count == K - 1:
			insertIndex = i
	if count == K:
		targetIndex = i
		break

pos = targetIndex
while True:
	S[insertIndex] = "1"
	S[pos] = "0"
	insertIndex += 1
	pos += 1
	if pos == N:
		break
	if S[pos] == "0":
		break

print("".join(S))
