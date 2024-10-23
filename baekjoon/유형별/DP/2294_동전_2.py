import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

coins = list(set(coins))
coins.sort()

dp = [-1] * (k+1)
for c in coins:
    if c <= k:
        dp[c] = 1

for i in range(coins[0], k+1):
    for c in coins:
        if i - c >= 0 and dp[i-c] > 0:
            if dp[i] > 0:
                dp[i] = min(dp[i], dp[i-c] + 1)
            else:
                dp[i] = dp[i-c] + 1

print(dp[-1])