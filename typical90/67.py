N, K = map(int, input().split())

if N == 0:
    print("0")
    exit()

def base_n(num_10,n):
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return int(str_n[::-1])

def base_10(num_n,n):
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10


for i in range(K):
    n10 = base_10(N, 8)
    n9 = str(base_n(n10, 9))
    N = int(n9.replace("8", "5"))

print(N)

