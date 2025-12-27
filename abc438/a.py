D, F = map(int, input().split())

while D > F:
    F += 7
print(F - D if F - D != 0 else 7)

