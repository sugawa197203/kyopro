import queue

N = int(input())

U, V = [], []

for i in range(N-1):
	u, v = map(int, input().split())
	U.append(u)
	V.append(v)

counts = []
checked = {1}

def getnexts(i):
	nexts = []
	for j in range(N-1):
		if U[j-1] == i and V[j-1] not in checked:
			nexts.append(V[j-1])
		if V[j-1] == i and U[j-1] not in checked:
			nexts.append(U[j-1])
	return nexts

start = getnexts(1)

if len(start) == 1:
	print(1)
	exit()

startlen = len(start)
q = queue.Queue()

for i, s in enumerate(start):
	q.put((s, i))

counts = [1] * startlen
life = [1] * startlen

while True:
	n, i = q.get()
	checked.add(n)
	life[i] -= 1
	counts[i] += 1
	nexts = getnexts(n)
	life[i] += len(nexts)
	
	_c = 0
	for _i in life:
		if _i != 0:
			_c += 1

	if _c <= 1:
		break


	for j in range(len(nexts)):
		q.put((nexts[j], i))

# for n1 in start:
# 	count = 2
# 	stack = getnexts(n1)
# 	checked.add(n1)
# 	while len(stack) > 0:
# 		n = stack.pop()
# 		checked.add(n)
# 		count += 1
# 		stack.extend(getnexts(n))
# 	counts.append(count)
flag = False
result = []
for l, c in zip(life, counts):
	if l == 0:
		result.append(c)
	else:
		flag = True

if flag:
	print(sum(result))
	exit()

result.sort()
c = result[0]

for i in range(1, len(result) - 1):
	c += result[i] - 1

print(c)
