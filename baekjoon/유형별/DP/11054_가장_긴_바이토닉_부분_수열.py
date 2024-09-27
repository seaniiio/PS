n = int(input())
nums = list(map(int, input().split()))
up_dp = [1] * n
down_dp = [1] * n

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            up_dp[i] = max(up_dp[i], up_dp[j] + 1)
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if nums[i] > nums[j]:
            down_dp[i] = max(down_dp[i], down_dp[j] + 1)
max_v = 1

for k in range(n):
    max_v = max(max_v, up_dp[k] + down_dp[k] - 1)

print(max_v)