H, W = map(int, input().split())
Grid = [list(map(int, input().split())) for _ in range(H)]

ans = 0

minimum = min([min(row) for row in Grid])

for row in Grid:
    for num in row:
        ans += num - minimum

print(ans)

