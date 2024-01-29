dp = list([0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] for _ in range(1001)) # 끝자리가 i로 끝나는 수의 개수
dp[1][1] = [1 for _ in range(10)]
dp[1][0] = 10
n = int(input())

for i in range(2, n + 1):
    for j in range(10):
        for k in range(j+1):
            dp[i][1][j] += dp[i-1][1][k]
    dp[i][0] = sum(dp[i][1]) % 10007

print(dp[n][0])
