H, W = map(int, input().split(" "))

cookie = []

for i in range(H):
	cookie.append(input())

l = []
_l = []

for c in cookie:
	a = c.count("#")
	l.append(a)
	if a != 0:
		_l.append((c.index("#"), len(c) - c[::-1].index("#") - 1))
	else:
		_l.append(None)
	
m = max(l)

migi_haji_flag = False
hidari_haji_flag = False
buf = None
for i in _l:
	if i == None:
		continue
	if buf == None:
		buf = i
		continue
	if buf[0] != i[0]:
		hidari_haji_flag = True
		break
	if buf[1] != i[1]:
		migi_haji_flag = True
		break


for i, n in enumerate(l):
	if n != 0 and n == m - 1:
		c = cookie[i]

		if hidari_haji_flag:
			a = c.index("#") - 1
			print(f"{i + 1} {a + 1}")
			break

		if migi_haji_flag:
			a = len(c) - c[::-1].index("#")
			print(f"{i + 1} {a + 1}")
			break

		flag = False
		for j, a in enumerate(c):
			if a == "#":
				flag = True
				continue
			if flag and a == ".":
				print(f"{i + 1} {j + 1}")
				exit(0)