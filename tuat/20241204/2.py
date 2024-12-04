N = int(input())
A = list(map(int, input().split()))

kirekomi = [0]

for a in A:
    kirekomi.append((kirekomi[-1] + a) % 360)
kirekomi.sort()
ans = 0
kakudo = []
for i in range(N):
    kakudo.append(kirekomi[i + 1] - kirekomi[i])
kakudo.append(360 - kirekomi[-1])
print(max(kakudo))