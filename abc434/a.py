W, B = map(int, input().split())

W *= 1000

sho, amari = divmod(W, B)

print(sho + 1)