X, Y = map(int, input().split())

ans = X + Y

if ans <= 12:
    print(ans)
    exit()

ans %= 12

print(ans if ans else 12)