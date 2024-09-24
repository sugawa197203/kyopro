H, W, M = map(int, input().split())

colors = dict()
h = 0
w = 0
hline = [0] * H
wline = [0] * W
TAX = []
filed = 0
for i in range(M):
	t, a, x = map(int, input().split())
	TAX.append((t, a, x))

for t, a, x in TAX[::-1]:
	if t == 1:
		if hline[a - 1] + h < W:
			hline[a - 1] = W
			w += 1
			colors.setdefault(x, 0)
			colors[x] += W - h
			filed += W - h
	else:
		if wline[a - 1] + w < H:
			wline[a - 1] = H
			h += 1
			colors.setdefault(x, 0)
			colors[x] += H - w
			filed += H - w

if filed != H * W:
	colors.setdefault(0, 0)
	colors[0] += H * W - filed

colorsList = list(colors.items())
colorsList.sort(key=lambda x: x[0])

print(len(colorsList))
for color, num in colorsList:
	print(color, num)
