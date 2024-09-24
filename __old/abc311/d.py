N, M = map(int, input().split(" "))
S = []

for i in range(N):
	S.append(input())

throgh = [[False] * M for i in range(N)]
throgh[1][1] = True

pos = (1, 1)


def getdirectpos(pos, direct):
	if direct == 0:
		return (pos[0] - 1, pos[1])
	elif direct == 1:
		return (pos[0], pos[1] + 1)
	elif direct == 2:
		return (pos[0] + 1, pos[1])
	elif direct == 3:
		return (pos[0], pos[1] - 1)

def getdata(pos):
	return S[pos[0]][pos[1]]

def gostrait(startpos, direct):
	pos = startpos
	while True:
		throgh[pos[0]][pos[1]] = True
		nextpos = getdirectpos(pos, direct)
		if getdata(nextpos) == '#':
			return pos
		pos = nextpos

def isenddirect(pos, direct):
	while True:
		nextpos = getdirectpos(pos, direct)
		if getdata(nextpos) == '#':
			return False
		elif not throgh[nextpos[0]][nextpos[1]]:
			return True
		pos = nextpos

# def do(pos):
# 	direction = []
# 	for i in range(4):
# 		if isenddirect(pos, i):
# 			if getdata(getdirectpos(pos, i)) == '.':
# 				direction.append(i)
	
	
# 	for d in direction:
# 		do(gostrait(pos, d))

stack = [(1, 1)]

# do(pos)

while True:
	if len(stack) == 0:
		break
	pos = stack.pop()
	direction = []
	for i in range(4):
		if isenddirect(pos, i):
			if getdata(getdirectpos(pos, i)) == '.':
				direction.append(i)
	if len(direction) == 0:
		continue
	elif len(direction) >= 1:
		stack.append(pos)

	pos = gostrait(pos, direction[0])
	stack.append(pos)

count = 0

for t in throgh:
	for tt in t:
		if tt:
			count += 1

print(count)
	
