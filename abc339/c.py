N = int(input())
A = list(map(int, input().split()))

now = 0
minimum = 0

for a in A:
	now += a
	minimum = min(minimum, now)

print(now-minimum)