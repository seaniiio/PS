n = int(input())
dp = [0] * 100001
dp[2], dp[3], dp[4], dp[5] = 1, 0, 2, 1

for i in range(6, n+1):
    if dp[i-2] == 0 and dp[i-5] == 0:
        dp[i] = 0
    elif dp[i-2] == 0:
        dp[i] = dp[i-5] + 1
    elif dp[i-5] == 0:
        dp[i] = dp[i-2] + 1
    else:
        dp[i] = min(dp[i-2] + 1, dp[i-5] + 1)

answer = -1 if dp[n] == 0 else dp[n]
print("dp:", dp[:15])
print(answer)
