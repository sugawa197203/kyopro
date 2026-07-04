

def solve(X, Y, K):
    if X == Y:
        return 0
    
    ans = 0
    
    while X != Y:
        if X > Y:
            X = X // K
            ans += 1
        else:
            Y = Y // K
            ans += 1

    return ans

T = int(input())
for _ in range(T):
    X, Y, K = map(int, input().split())
    print(solve(X, Y, K))
