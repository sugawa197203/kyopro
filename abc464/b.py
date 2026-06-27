H, W = map(int, input().split())
C = [input() for _ in range(H)]

ans = []

top = 0
for i in range(H):
    if all(c == '.' for c in C[i]):
        continue
    top = i
    break

under = H
for i in range(H - 1, -1, -1):
    if all(c == '.' for c in C[i]):
        continue
    under = i
    break


left = 0
for i in range(W):
    if all(C[j][i] == '.' for j in range(top, under + 1)):
        continue
    left = i
    break

right = W
for i in range(W - 1, -1, -1):
    if all(C[j][i] == '.' for j in range(top, under + 1)):
        continue
    right = i
    break


for i in range(top, under + 1):
    ans.append(C[i][left:right + 1])

for i in range(len(ans)):
    print(ans[i])
