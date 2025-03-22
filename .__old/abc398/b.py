A = list(map(int, input().split()))

from collections import Counter

ac = Counter(A)

two = False
three = False

for v in ac.values():
	if not three and 3 <= v:
		three = True
	elif not two and 2 <= v:
		two = True

print("Yes" if two and three else "No")
