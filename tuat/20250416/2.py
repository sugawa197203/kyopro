N = int(input())
Grid = [list(map(int, list(input()))) for _ in range(N)]

ans = 0
for x in range(N):
    for y in range(N):
        for direction in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            num = []
            start = (x, y)
            for i in range(N):
                num.append(Grid[start[0]][start[1]])
                start = (start[0] + direction[0], start[1] + direction[1])
                if start[0] < 0 or start[0] >= N or start[1] < 0 or start[1] >= N:
                    break
