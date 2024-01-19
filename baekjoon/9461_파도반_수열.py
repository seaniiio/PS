dp = [0 for _ in range(102)]
dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
dp[6] = 3

n = int(input())
for _ in range(n):
    k = int(input())
    for i in range(7, k+1):
        dp[i] = dp[i-1] + dp[i-5]
    print(dp[k])