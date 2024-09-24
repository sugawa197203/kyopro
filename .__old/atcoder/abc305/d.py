N = int(input())
A = list(map(int, input().split(" ")))
Q = int(input())
L, R = [], []

for i in range(Q):
	l, r = map(int, input().split(" "))
	L.append(l)
	R.append(r)
	
import bisect

for l, r in zip(L, R):
	sleepTime = 0
	
	l_index = bisect.bisect_right(A, l)
	start_sleep_flag = l_index % 2 == 0
	if start_sleep_flag:
		sleepTime += A[l_index] - l
		# print(">START", sleepTime, l_index, A[l_index])
	
	
	r_index = bisect.bisect_left(A, r) - 1
	end_sleep_flag = r_index % 2 != 0
	if end_sleep_flag:
		sleepTime += r - A[r_index]
		# print(">END", sleepTime, r_index, A[r_index])
	

	sleepFlag = not start_sleep_flag

	# print("l_ind", l_index)
	# print("r_ind", r_index)
	# print(A[l_index:r_index-1], A[l_index+1:r_index])
	for timeA, timeB in zip(A[l_index:r_index], A[l_index+1:r_index+1]):
		if sleepFlag:
			sleepTime += timeB - timeA
			# print("SLEEEP", timeA, timeB)
		sleepFlag = not sleepFlag

	print(sleepTime)

	
	
