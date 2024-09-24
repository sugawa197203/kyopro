N, T = map(int, input().split())
A = list(map(int, input().split()))

yoko = [0] * N
tate = [0] * N
sagari = 0
agari = 0

for turn, a in enumerate(A):
	tateI, yokoI = divmod(a - 1, N)
	tate[tateI] += 1
	yoko[yokoI] += 1
	if tateI == yokoI:
		sagari += 1
	if tateI == N - yokoI - 1:
		agari += 1
	if tate[tateI] == N or yoko[yokoI] == N or sagari == N or agari == N:
		print(turn + 1)
		exit()

print(-1)
