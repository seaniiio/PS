# 가장 긴 증가하는 부분수열
# 1000 * 1000

dp = [1] * 1000
n = int(input())
box = list(map(int, input().split()))

for i in range(n):
    for j in range(i):
        if box[j] < box[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))