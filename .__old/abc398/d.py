N, R, C = map(int, input().split())
S = input()

direct = {
	"N": (1, 0),
	"E": (0, -1),
	"S": (-1, 0),
	"W": (0, 1)
}

smoke = dict()

takibi = (0, 0)
takahashi = (R, C)
ans = []
for s in S:
	smoke[takibi] = True
	takibi = (takibi[0] + direct[s][0], takibi[1] + direct[s][1])
	takahashi = (takahashi[0] + direct[s][0], takahashi[1] + direct[s][1])
	ans.append("1" if takahashi in smoke else "0")

print("".join(ans))
