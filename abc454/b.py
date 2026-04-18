N, M = map(int, input().split())
F = list(map(int, input().split()))
a = [0] * M

for f in F:
    a[f - 1] += 1

if all(x <= 1 for x in a):
    print("Yes")
else:
    print("No")

if 0 in a:
    print("No")
else:
    print("Yes")
