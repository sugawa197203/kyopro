N, K = map(int, input().split())
colors, value = [], []
for _ in range(N):
	c, v = map(int, input().split())
	colors.append(c)
	value.append(v)

from pulp import *

model = LpProblem(sense=LpMaximize)
selectBall = [LpVariable(f'ball{i}', cat=LpBinary) for i in range(N)]
# max to sum of value
model += lpDot(value, selectBall)
# select N-K balls
model += lpSum(selectBall) == (N - K)
# Adjacent colors are not the same
for i in range(N):
	for j in range(i+1, N):
		model += (colors[i] != colors[j]) | (selectBall[i] + selectBall[j] <= 1)

model.solve()
print(int(value(model.objective.value())))

