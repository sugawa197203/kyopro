N, D = map(int, input().split())
A = list(map(int, input().split()))

C = [0] * (10**6 + 1)

for a in A:
	C[a] += 1

ans = 0
if D == 0:
	for i in range(10**6):
		if 1 < C[i]:
			ans += C[i]
			C[i] = 0
	
	print(ans)
	exit(0)

from collections import Counter

ans = 0
CC = Counter(A)
effect = [0] * (10**6 + 1)
mosteffect = []
# print(CC)
for i in range(10**6 + 1):
	if C[i] == 0:
		continue
	if i < D:
		effect[i] = CC[i + D]
	elif 10**6 - D < i:
		effect[i] = CC[i - D]
	else:
		effect[i] = CC[i + D] + CC[i - D]
	mosteffect.append((i, effect[i]))

mosteffect.sort(key=lambda x: x[1], reverse=True)
# print(mosteffect)

for v, count in mosteffect:
	if effect[v] == 0:
		continue
	if v < D:
		if C[v - D] > C[v]:
			continue
	if not 10**6 - D <= v:
		if C[v + D] > C[v]:
			continue
	if D <= v and v <= 10**6 - D:
		if C[v - D] == 0 and C[v + D] == 0:
			continue
	# print(f"v: {v}, count: {count}, C: {C[:10]}, effect: {effect[:10]}")
	ans += C[v]
	C[v] = 0
	effect[v] = 0
	if D < v:
		effect[v - D] -= CC[v]
	if not 10**6 - D <= v:
		effect[v + D] -= CC[v]
# 	print(f"v: {v}, count: {count}, C: {C[:10]}, effect: {effect[:10]}")
# print(f"C: {C[:10]}, effect: {effect[:10]}")
print(ans)