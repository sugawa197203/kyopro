p, q = input().split(" ")

l = {'A':0, 'B':3, 'C':4, 'D':8, 'E':9, 'F':14, 'G':23}

p_ = l[p]
q_ = l[q]

print(abs(p_ - q_))
