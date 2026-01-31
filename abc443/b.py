N, K = map(int, input().split())

n = 0

for i in range(10**8 + 10):
    n += N + i
    if n >= K:
        print(i)
        break

