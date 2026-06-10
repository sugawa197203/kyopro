X = int(input())
a = "HelloWorld"
X -= 1
for i in range(len(a)):
    if i != X:
        print(a[i], end="")