N = int(input())
if N < 1000:
    print(0)
    exit()

l = len(str(N))
cnt = (l - 1) // 3
ans = N % (10 ** (3 * cnt)) * cnt + 1
print(f"{N=}, {ans=}, {cnt=}")
print((N // (10 ** (3 * cnt)) - 1) * (10 ** (3 * cnt)) * cnt)
ans += (N // (10 ** (3 * cnt)) - 1) * (10 ** (3 * cnt)) * cnt
N %= 10 ** (3 * cnt)
cnt -= 1
print(f"{N=}, {ans=}, {cnt=}")
while cnt > 0:
    cnt -= 1
    ans += 999 * (10 ** (3 * cnt)) * (cnt + 1)
    print(N, ans, cnt)

print(ans)
