S = input()
N = len(S)

ans = 0

for i in range(N):
    if S[i] == 'C':
        i += 1
        count = min(i, N - i + 1)
        # print(f'i: {i}, count: {count}')
        ans += count

print(ans)
