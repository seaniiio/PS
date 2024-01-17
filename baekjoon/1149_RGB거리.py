n = int(input())
dp = [[0, 0, 0] for _ in range(n)]
h = []

for i in range(n):
    l = list(map(int, input().split()))
    h.append(l)

dp[0] = h[0]

for i in range(1, n):
    dp[i][0] = min(h[i][0] + dp[i-1][1], h[i][0] + dp[i-1][2])
    dp[i][1] = min(h[i][1] + dp[i-1][0], h[i][1] + dp[i-1][2])
    dp[i][2] = min(h[i][2] + dp[i-1][0], h[i][2] + dp[i-1][1])

print(min(dp[-1]))