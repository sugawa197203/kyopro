H = int(input())
day = 1
h = 1
while H >= h:
	h += 2 ** day
	day += 1
print(day)