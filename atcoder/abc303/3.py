N, M, H, K = [int(i) for i in input().split(" ")]
S = input()
ITEM = dict()
 
for i in range(M):
	x, y = [int(p) for p in input().split(" ")]
 
	ITEM[(x, y)] = True
 
X = 0
Y = 0
#print("----")
for s in S:
 
	#print("-")
	#print("X Y", X, Y)
	#print("H", H)
 
	if H == 0:
		print("No")
		exit(0)
	H -= 1
 
	if s == "R":
		X += 1
	elif s == "L":
		X -= 1
	elif s == "U":
		Y += 1
	elif s == "D":
		Y -= 1
	
	if H < K:
		index = ITEM.get((X, Y), False)
		if index:
			ITEM[(X, Y)] = False
			#print("UP", H)
			H = K
	
print("Yes")