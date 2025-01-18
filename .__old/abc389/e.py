def max_items(N, M, P):
    def can_buy(k, p, budget):
        # 商品 i を k 個買えるかを判定する
        return k * k * p <= budget
    
    total_items = 0
    for price in P:
        low, high = 0, int((M // price)**0.5) + 1
        while low < high:
            mid = (low + high + 1) // 2
            if can_buy(mid, price, M):
                low = mid
            else:
                high = mid - 1
        total_items += low
        M -= low * low * price  # 残りの予算を更新
        if M < 0:
            break

    return total_items

# 入力処理
N, M = map(int, input().split())
P = list(map(int, input().split()))

# 出力
print(max_items(N, M, P))
