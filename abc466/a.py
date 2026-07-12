N = int(input())
X = list(map(int, input().split()))

print("Yes" if all(x < 0 for x in X) else "No")
