T = int(input())
for i in range(T):
    N, M, K = map(int, input().split())
    if N - 1 == K:
        print(K * M + M + 1)
    else:
        print(K * M + M)
