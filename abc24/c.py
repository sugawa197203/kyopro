N, D, K = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in range(D)]
ST = [tuple(map(int, input().split())) for _ in range(K)]

for s, t in ST:
    count = 0
    left = right = s
    for l, r in LR:
        count += 1
        if r < left or right < l:
            continue
        left = min(left, l)
        right = max(right, r)
        if left <= t <= right:
            print(count)
            break

