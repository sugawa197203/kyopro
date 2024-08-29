N = int(input())
A = list(map(int, input().split()))

humidaitotal = 0
nowtakasa = 0

for a in A:
    if a > nowtakasa:
        nowtakasa = a
    else:
        humidaitotal += nowtakasa - a

print(humidaitotal)
