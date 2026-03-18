N = int(input())
S = input()

ans = 0
count = 0

for s in S:
    if s == "o":
        count += 1
    else:
        ans = max(ans, count)
        count = 0

ans = max(ans, count)
print(ans)
