N = int(input())
A = list(map(int, input().split()))

apiered = [0] * (N+1)
anses = [0] * (N+1)
temps = 0

def com(n):
    return (n * (n - 1)) // 2

for i, a in enumerate(reversed(A)):
    b = com(apiered[a])
    anses[i] = temps - b
    apiered[a] += 1
    temps += com(apiered[a]) - b



print(sum(anses))
