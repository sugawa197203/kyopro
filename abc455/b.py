H, W = map(int, input().split())
S = [input() for _ in range(H)]

ans = 0

for h1 in range(H):
    for w1 in range(W):
        for h2 in range(h1, H):
            for w2 in range(w1, W):
                if h1 == h2 and w1 == w2:
                    ans += 1
                    continue
                
                flag = True
                for i in range(h1, h2 + 1):
                    for j in range(w1, w2 + 1):
                        if S[i][j] != S[h1 + h2 - i][w1 + w2 - j]:
                            flag = False
                            break
                    if not flag:
                        break
                else:
                    ans += 1

print(ans)
