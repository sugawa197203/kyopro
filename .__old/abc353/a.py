N = int(input())
H = list(map(int, input().split()))
I = -1
m = H[0]
for i, h in enumerate(H):
	if i == 0:
		continue
	if m < h:
		m = h
		print(i+1)
		exit()

print(-1)
