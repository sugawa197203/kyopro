T = int(input())

def ok(a:int, b:int, c:int, k:int) -> bool:
    # print(a, b, c, k)
    ac = min(a, c)
    if ac < k:
        return False
    amari = a + b + c - 2 * k
    if amari < k:
        return False
    return True


def solve(a:int, b:int, c:int):
    left, right = 0, 10**9 + 1
    while left < right:
        # print(left, right)
        mid = (left + right) // 2
        if ok(a, b, c, mid):
            left = mid + 1
        else:
            right = mid
    print(left - 1)

for _ in range(T):
    a, b, c = map(int, input().split())
    solve(a, b, c)
