N, K = map(int, input().split())
colors:list[int]
value:list[int]
colors, value = [], []

for _ in range(N):
	c, v = map(int, input().split())
	colors.append(c)
	value.append(v)

import pulp

model = pulp.LpProblem(sense=pulp.LpMaximize)
selectBall = [pulp.LpVariable(f'ball{i}', cat=pulp.LpBinary) for i in range(N)]
# max to sum of value
model += pulp.lpDot(value, selectBall)
# select N-K balls
model += pulp.lpSum(selectBall) == (N - K)
# Adjacent colors are not the same after selection
for i in range(N):
	for j in range(i+1, N):
		model += (colors[i] != colors[j]) | (pulp.lpSum([selectBall[i].value(), selectBall[j].value()]) <= 1)

model.solve()
print(int(value(model.objective.value())))

