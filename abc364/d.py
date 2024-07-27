N, Q = map(int, input().split())
a = list(map(int, input().split()))
import bisect
a.sort()
print(a)
for i in range(Q):
	b, k = map(int, input().split())
	bind = bisect.bisect_right(a, b)
	left = 0
	right = N-1
	mid = (left + right) // 2

	while True:
		print(left, right)
		if right - left == k:
			print(left, right, b, max(abs(a[left]-b), abs(a[right-1]-b)))
			break

		if right - left > k:
			if b - a[left] >= a[right] - b:
				left += (bind - left) // 2
				mid = (left + right) // 2
			else:
				right -= (right - bind) // 2
				mid = (left + right) // 2
		else:
			if b - a[left] >= a[right] - b:
				if left == 0:
					right += 1
					mid = (left + right) // 2
				else:
					left -= (bind - left) // 2
					mid = (left + right) // 2
			else:
				if right == N-1:
					left -= 1
					mid = (left + right) // 2
				else:
					right += (right - bind) // 2
					mid = (left + right) // 2
