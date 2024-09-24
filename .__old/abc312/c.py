import bisect
 
input()
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))
 
A.sort()
B.sort()

# 売り手の最低額が、買い手の最高額
# 売る気無いのは省く
# 3 3
# 2 2 2
# 1 1 1
if A[0] > B[-1]:
	print(B[-1] + 1)
	exit(0)

for ind, a in enumerate(A):

	# 1 2 3
	# 1 1
	if a > B[-1]:
		print(B[-1] + 1)
		exit(0)

	# にぶたん
	i = bisect.bisect_left(B, a)

	# 1 2 3
	# 1 2 3
	if ind + 1 >= len(B) - i: # 売り手が買い手以上
		print(a)
		exit(0)

#
# 1
# 1 1
print(B[-1] + 1)