H, W = map(int, input().split())

bmi = W / (H * H) * 10000.0
print("Yes" if bmi >= 25.0 else "No")
