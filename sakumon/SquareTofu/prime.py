def isprime(N):
    if N < 2:
        return False
    i = 2
    while i * i <= N:
        if N % i == 0:
            return False
        i += 1
    return True

# 入力と判定
N = int(input())

# N 以下の素数を探す
result = -1
for i in range(N, 1, -1):
    if isprime(i):
        result = i
        break
print(result)