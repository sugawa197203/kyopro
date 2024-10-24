def solve(N, M):
    # DP配列の初期化
    dp = [0] * M
    dp[0] = 1  # 空集合の部分和は 0 とする

    # 各国民番号で DP 配列を更新
    for i in range(1, N + 1):
        new_dp = dp[:]  # dp配列のコピーを作成
        for r in range(M):
            new_dp[(r + i) % M] += dp[r]
        dp = new_dp  # 更新された dp を反映

    # 答えは dp[0] に格納されている（和が M で割り切れる部分集合の数）
    print(dp[0] - 1)  # 空集合を除くために -1 する

# 入力の読み込み
N, M = map(int, input().split())
solve(N, M)
