# DP
# n-3칸 -> n-1칸 -> n칸
# n-2칸 -> n칸
# dp[n] = max(score[n] + score[n-1] + dp[n-3], score[n] + dp[n-2])

n = int(input())
score = [0] * 301
dp = [0] * 301
for i in range(1, n+1):
    score[i] = int(input())

dp[1] = score[1]
dp[2] = score[1] + score[2]
dp[3] = max(score[3] + score[2], score[3] + score[1])

for j in range(4, n+1):
    dp[j] = max(score[j] + score[j-1] + dp[j-3], score[j] + dp[j-2])

print(dp[n])