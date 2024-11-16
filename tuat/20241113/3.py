N = int(input())

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i ^ 2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True

if N == 1:
    print("Not Prime")
    exit()
elif N == 2 or N == 3 or N == 5:
    print("Prime")
    exit()

if is_prime(N):
    print("Prime")
elif N % 2 != 0 and N % 5 != 0 and sum(map(int, list(str(N)))) % 3 != 0:
    print("Prime")
else:
    print("Not Prime")
