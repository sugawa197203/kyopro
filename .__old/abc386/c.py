K = int(input())
S = list(input())
T = list(input())
if abs(len(S) - len(T)) > 1:
	print("No")
	exit()
candelete = len(S) - len(T) == 1
caninsert = len(T) - len(S) == 1
ind = 0

si, ti = 0, 0
while si < len(S) and ti < len(T):
	if S[si] == T[ti]:
		si += 1
		ti += 1
		continue
	if K == 0:
		print("No")
		exit()
	if not candelete and not caninsert:
		# replace
		K -= 1
		si += 1
		ti += 1
		continue
	if candelete:
		# delete
		K -= 1
		si += 1
		continue
	if caninsert:
		# insert
		K -= 1
		ti += 1
		continue



print("Yes")
