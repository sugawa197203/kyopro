N = int(input())
S = input()

a = 0
b = 0
c = 0

for i, s in enumerate(S):
	if s == 'A':
		a += 1
	elif s == 'B':
		b += 1
	elif s == 'C':
		c += 1
	
	if 0 < a and 0 < b and 0 < c:
		print(i + 1)
		exit()
	