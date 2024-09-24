S = input()

before = S[0]
bbefore = S[0]
beforeIndex = 0
ans = 0
beforeCount = 0

def iswin(_a, _b):
    if _a == "R":
        if _b == "S":
            return True
        else:
            return False
    elif _a == "S":
        if _b == "P":
            return True
        else:
            return False
    else:
        if _b == "R":
            return True
        else:
            return False

for i in range(len(S)):
    if before != S[i]:
        beforeCount = i - beforeIndex
        beforeIndex = i
        before = S[i]
        break

for i in range(beforeIndex+1, len(S)):
    if before != S[i]:
        if beforeCount % 2 == 0:
            ans += beforeCount // 2
        else:
            ans += beforeCount // 2 + 1
            
        beforeCount = i - beforeIndex
        beforeIndex = i

        
