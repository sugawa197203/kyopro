N = int(input())
C = [list(map(int, input().split())) for _ in range(N - 1)]
for a in range(N - 2):
    for c in range(a + 2, N):
        for b in range(a + 1, c):
            if C[a][c-a-1] > C[a][b-a-1] + C[b][c-b-1]:
                print("Yes")
                exit()

print("No")
