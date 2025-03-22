N = int(input())
from collections import defaultdict
G = defaultdict(list)
for i in range(N-1):
	u, v = map(int, input().split())
	G[u].append(v)
	G[v].append(u)

def update_distance():
	distance = [[-1] * (N+1) for _ in range(N+1)]
	for start in range(1, N+1):
		stack = [start]
		distance[start][start] = 0
		while stack:
			node = stack.pop()
			for nextnode in G[node]:
				if distance[start][nextnode] == -1:
					distance[start][nextnode] = distance[start][node] + 1
					stack.append(nextnode)
	return distance

# def print_distance(distance):
# 	for d in distance[1:]:
# 		print(d[1:])

def count_odd(distance):
	odd = 0
	for d in distance[1:]:
		for dd in d[1:]:
			if 3 <= dd and dd % 2 == 1:
				odd += 1
	return odd // 2

def get_grateer3_distance(distance):
	for i in range(1, N+1):
		for j in range(i+1, N+1):
			if 3 <= distance[i][j] and distance[i][j] % 2 == 1:
				return (i, j)

nodedistance = update_distance()

if count_odd(nodedistance) % 2 == 0:
	print("Second")
else:
	print("First")
	(u, v) = get_grateer3_distance(nodedistance)
	print(u, v)
	G[u].append(v)
	G[v].append(u)
	nodedistance = update_distance()

while True:
	u, v = map(int, input().split())
	if u == -1 and v == -1:
		break
	
	G[u].append(v)
	G[v].append(u)
	nodedistance = update_distance()
	(u, v) = get_grateer3_distance(nodedistance)
	print(u, v)
	G[u].append(v)
	G[v].append(u)
	nodedistance = update_distance()


	
