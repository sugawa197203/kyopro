N, M = map(int, input().split())
Ryouri = []
for _ryori in range(M):
	k, *sozais = map(int, input().split())
	Ryouri.append(sozais)
Kokuhuku = list(map(int, input().split()))

OKcount = 0

ryouriBySozai = [[] for _ in range(N)]
nigateCount = [0] * M

for _ryori in range(M):
	sozais = Ryouri[_ryori]
	for sozai in sozais:
		ryouriBySozai[sozai - 1].append(_ryori)
		nigateCount[_ryori - 1] += 1

for _ryori in range(M):
	if nigateCount[_ryori] == 0:
		OKcount += 1

for kokuhuku in Kokuhuku:
	for ryouri in ryouriBySozai[kokuhuku - 1]:
		nigateCount[ryouri - 1] -= 1
		if nigateCount[ryouri - 1] == 0:
			OKcount += 1
	print(OKcount)

