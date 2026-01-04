N = int(input())

count = [0] * (10**7+1)

for x in range(1, 10**4):
    if x**2 > N:
        break
    for y in range(x+1, 10**4):
        n = x**2 + y**2
        if n > N:
            break
        count[n] += 1

ans = []
for i in range(1, N+1):
    if count[i] == 1:
        ans.append(i)

print(len(ans))
print(*ans)
