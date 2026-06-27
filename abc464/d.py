

def solve(N: int, S: list[str], X: list[int], Y: list[int]) -> int:
    if S[0] == 'R':
        dpAme = 0
        dpHare = -X[0]
    else:
        dpAme = -X[0]
        dpHare = 0

    for i in range(1, N):
        if S[i] == 'R':
            costR = 0
        else:
            costR = -X[i]

        if S[i] == 'S':
            costS = 0
        else:
            costS = -X[i]

        nextR = max(dpAme, dpHare) + costR

        nextS = max(dpAme + Y[i - 1], dpHare) + costS

        dpAme = nextR
        dpHare = nextS

    return max(dpAme, dpHare)


T = int(input())
for _ in range(T):
    N = int(input())
    S = list(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))

    print(solve(N, S, X, Y))
