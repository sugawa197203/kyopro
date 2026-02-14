N = int(input())

SS = [input() for _ in range(N)]

m = max(map(len, SS))
for s in SS:
    print(s.center(m, '.'))
