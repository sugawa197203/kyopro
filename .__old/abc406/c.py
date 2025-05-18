N = int(input())
P = list(map(int, input().split()))

yamaindex = 1
taniindex = 2
ans = 0

def tani(a, b, c):
	return a > b < c

def yama(a, b, c):
	return a < b > c

while taniindex < N - 1:
	# print(f"{yamaindex=}, {taniindex=}, {ans=}")
	# input()
	if not tani(P[taniindex - 1], P[taniindex], P[taniindex + 1]):
		taniindex += 1
		if taniindex == N:
			break
		continue
	while yamaindex < taniindex:
		if yama(P[yamaindex - 1], P[yamaindex], P[yamaindex + 1]):
			break
		yamaindex += 1
		continue
	
	if yamaindex == taniindex:
		taniindex += 1
		continue
	maxleft = yamaindex - 1
	maxright = taniindex + 1
	leftcount = 0
	rightcount = 0
	while maxleft >= 0 and P[maxleft] < P[maxleft + 1]:
		leftcount += 1
		maxleft -= 1
	while maxright < N and P[maxright - 1] < P[maxright]:
		rightcount += 1
		maxright += 1
	
	# print(f"{yamaindex=}, {taniindex=}, {maxleft=}, {maxright=}, {leftcount=}, {rightcount=}")
	ans += leftcount * rightcount
	if maxleft == 0 and maxright == N:
		break
	taniindex += 1
	yamaindex += 1
	
print(ans)