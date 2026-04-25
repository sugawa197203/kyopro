from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))

AC = Counter(A).items()
AC = [a * b for a, b in AC]
AC.sort(reverse=True)
lenac = len(AC)
for i in range(min(K, lenac)):
    AC[i] = 0

print(sum(AC))
