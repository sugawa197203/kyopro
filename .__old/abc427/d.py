T = int(input())

def solve(N, M, K, S, edges):
    pass

for _ in range(T):
    n, m, k = map(int, input().split())
    s = input()
    _edges = [tuple(map(int, input().split())) for _ in range(m)]
    solve(n, m, k, s, _edges)
    
