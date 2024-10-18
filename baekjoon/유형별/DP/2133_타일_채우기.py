n = int(input())
dp = [0] * 31

dp[2] = 3

for i in range(4, n+1):
    if i % 2 == 1:
        continue
    dp[i] = dp[i-2] * 3
    for j in range(i-4, -1, -2):
        if j % 2 == 0:
            dp[i] += dp[j] * 2 # 2가 특수한 경우
    dp[i] += 2
print(dp[n])