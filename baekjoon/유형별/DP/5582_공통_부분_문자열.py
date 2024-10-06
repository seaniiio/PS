# import sys
# sys.setrecursionlimit(10 ** 6)

str_a = input().strip()
str_b = input().strip()

before_dp = [0] * len(str_a)
max_v = 0
for i in range(len(str_b)):
    dp = [0] * len(str_a)
    for j in range(len(str_a)):
        if str_a[j] == str_b[i]:
            if j == 0 or i == 0:
                dp[j] = 1
            else:
                dp[j] = before_dp[j-1] + 1
            max_v = max(max_v, dp[j])
    before_dp = dp[:]

print(max_v)