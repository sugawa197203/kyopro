N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(M)]

d = N - M

for i in range(d + 1):
	for j in range(d + 1):
		flag = True
		for k in range(M):
			for l in range(M):
				if S[i + k][j + l] != T[k][l]:
					flag = False
					break
			if not flag:
				break
		if flag:
			print(f"{i+1} {j+1}")
			exit()