# dp[k] = dp[k-1] + dp[k-2] + dp[k-3]

t = int(input())
dp = [0] * (1000000)
dp[1], dp[2], dp[3] = 1, 2, 4
for k in range(4, 1000000):
    dp[k] = (dp[k-1] + dp[k-2] + dp[k-3]) % 1000000009
for _ in range(t):
    n = int(input())
    print(dp[n])