N, M = map(int, input().split(' '))
C = input().split(' ')
D = input().split(' ')
P = list(map(int, input().split(' ')))

price = dict()
default = P[0]

P = P[1:]

for d, p in zip(D, P):
    price[d] = p

pricesum = 0

for c in C:
    if c in price:
        pricesum += price[c]
    else:
        pricesum += default

print(pricesum)
