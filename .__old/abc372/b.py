M = int(input())

A = []
l = list(range(20, -1, -1))

i = 0
while M > 0:
    if M >= 3**l[i]:
        A.append(l[i])
        M -= 3**l[i]
        continue
    i += 1

print(len(A))
print(*A)