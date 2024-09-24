A1, A2, A3 = map(int, input().split(" "))

task2 = abs(A2 - A1)
task3 = abs(A3 - A1)

task23 = task2 + abs(A3 - A2)
task32 = task3 + abs(A2 - A3)

print(task23 if task23 < task32 else task32)
