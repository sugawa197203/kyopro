A = list(map(int, input().split()))
import copy
sortedA = sorted(A)
for i in range(4):
	_A = copy.deepcopy(A)
	_A[i], _A[i+1] = _A[i+1], _A[i]
	if _A == sortedA:
		print("Yes")
		exit()

print("No")