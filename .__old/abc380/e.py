import bisect

N, Q = map(int, input().split())

colorBoder = {}
for i in range(N):
	colorBoder[i] = (i+1, i+1)

for q in range(Q):
	query = list(map(int, input().split()))
	if query[0] == 1:
		x = query[1]
		c = query[2]
		values = list(colorBoder.values())
		keys = list(colorBoder.keys())
		print("1", keys)
		xcolorInd = bisect.bisect_left(values, x, key=lambda __v: __v[1])
		xcolor = values[xcolorInd]

		print(2, colorBoder, xcolorInd, xcolor, (c, x), keys[xcolorInd])
		xcolor = (c, x)
		colorBoder[keys[xcolorInd]] = xcolor
		print(3, colorBoder, keys, colorBoder[keys[xcolorInd-1]][0], c)
		if xcolorInd-1 in keys and colorBoder[keys[xcolorInd-1]][0] == c:
			colorBoder.pop(keys[xcolorInd-1])
		if xcolorInd+1 in keys and colorBoder[keys[xcolorInd+1]][0] == c:
			colorBoder.pop(keys[xcolorInd+1])
		print(4, colorBoder)
		print()

