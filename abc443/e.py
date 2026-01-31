from collections import deque

def solve(N:int, C:int, S:list[str]):
    breakable = [True] * N
    S[N - 1][C - 1] = '*'
    for n in range(N):
        breakable[n] = S[N - 1][n] != '#'
    print(breakable)
    for n in range(N - 2, -1, -1):
        for c in range(C):
            if c < N - 1 and S[n-1][c + 1] == '*' :
                if S[n][c] == '.':
                    S[n][c] = '*'
                elif S[n][c] == '#' and breakable[n + 1]:
                    S[n][c] = '*'
                else:
                    breakable[n] = False
            if S[n-1][c] == '*':
                if S[n][c] == '.':
                    S[n][c] = '*'
                elif S[n][c] == '#' and breakable[n + 1]:
                    S[n][c] = '*'
                else:
                    breakable[n] = False
            if c > 0 and S[n-1][c - 1] == '*':
                if S[n][c] == '.':
                    S[n][c] = '*'
                elif S[n][c] == '#' and breakable[n + 1]:
                    S[n][c] = '*'
                else:
                    breakable[n] = False
    
    for n in range(N):
        print("".join(S[n]))
    for n in range(N):
        print("1" if S[0][n] == '*' else "0", end='')
    print()




__T__ = int(input())
for _ in range(__T__):
    print("----------")
    N, C = map(int, input().split())
    S = [list(input()) for _ in range(N)]
    print(f"N={N}, C={C}, S={S}")
    solve(N, C, S)