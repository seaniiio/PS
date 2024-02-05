n = int(input())
l = list(map(int, input().split()))
dp = [0] * n
dp[0] = l[0]

for i in range(1, n):
    m = l[i]
    for j in range(i):
        now = dp[j] + l[i]
        if l[i] > l[j]:
            m = max(m, now)
    dp[i] = m
print(max(dp))