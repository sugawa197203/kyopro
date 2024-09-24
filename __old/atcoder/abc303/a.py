def a(x, y):
    if x == y:
        return True
    if x == '1' and y == 'l':
        return True
    if y == '1' and x == 'l':
        return True
 
    if x == '0' and y == 'o':
        return True
    if y == '0' and x == 'o':
        return True
    return False


N = int(input())

S = input()
T = input()


for i in range(N):
    if not a(S[i], T[i]):
        print("No")
        exit(0)
        
print("Yes")