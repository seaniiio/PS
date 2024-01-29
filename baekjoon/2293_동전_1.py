n, k = map(int, input().split())
coins = []
dp = [0] * 10001
dp[0] = 1
for _ in range(n):
    c = int(input())
    if c <= k:
        coins.append(c)
coins.sort()

for c in coins:
    for i in range(c, k+1):
        if c <= k:
            dp[i] += dp[i - c]
print(dp[k])
            


