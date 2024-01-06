def solution(n):
    dp = [0] * 1000000
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return (dp[n] % 1234567)

# 대표적인 dp 문제