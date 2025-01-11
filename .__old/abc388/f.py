N, M, A, B = map(int, input().split())
L, R = [0]*M, [0]*M
for i in range(M):
	L[i], R[i] = map(int, input().split())

maxlen = B
minlen = A

for LR in zip(L, R):
	lenLR = LR[1] - LR[0]
	if maxlen < lenLR:
		print("No")
		exit()

# はじめのRと最後のLはスキップ
for RL in zip(R, L[1:]):
	lenRL = RL[0] - RL[1]
	if lenRL < minlen:
		minlen = lenRL
