from collections import defaultdict

H, W, K = map(int, input().split())
S = [[int(c) for c in input()] for _ in range(H)]

ans = 0

for up in range(H):
    acc = [0] * W
    for down in range(up, H):
        for c in range(W):
            acc[c] += S[down][c]

        print(up, down, acc)
        count = defaultdict(int)
        count[0] = 1
        total = 0
        _ans = 0
        for a in acc:
            total += a
            _ans += count[total - K]
            count[total] += 1
        print(total, count, _ans)
        ans += _ans


print(ans)
