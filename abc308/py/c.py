N = int(input())

out = []

for i in range(N):
    a, b = map(int, input().split(' '))
    out.append((i, a / (a + b)))

out.sort(key=lambda x: x[1], reverse=True)

for o in out:
    print(o[0] + 1, end=' ')