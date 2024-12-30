import math

n, x, y = map(int,input().split())

count_all = n//x + n//y - n//(math.lcm(x,y))

print(int(count_all))