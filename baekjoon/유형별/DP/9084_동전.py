# 작은거부터 -> 겹치는 경우가 없게
# dp[1][1000] -> 첫번째 동전으로 만들 수 있는 1000원의 가지수

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    won = int(input())

    dp = [[0] * (won+1) for _ in range(n+2)]
    for i in range(n+2):
        dp[i][0] = 1
    for i, coin in enumerate(coins):
        for j in range(1, won+1): # j원
            dp[i+1][j] = dp[i][j]
            if j - coin >= 0:
                dp[i+1][j] += dp[i+1][j-coin]
    print(dp[n][won])