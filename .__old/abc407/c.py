from collections import deque
S = input()
n = len(S)
S = deque(S)
ans = 0
mind = 0
while S:
	if mind != 0:
		_s = int(S[-1])
		if _s >= mind:
			S[-1] = str(_s - mind)
		else:
			S[-1] = str(_s + 10 - mind)
	if S[-1] == '0':
		S.pop()
		ans += 1
	else:
		c = int(S[-1])
		ans += c + 1
		mind = (mind + c) % 10
		S.pop()


print(ans)