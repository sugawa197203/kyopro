N = int(input())
T = input()
A = input()

for t, a in zip(T, A):
	if t == 'o' and a == 'o':
		print('Yes')
		break
else:
	print('No')