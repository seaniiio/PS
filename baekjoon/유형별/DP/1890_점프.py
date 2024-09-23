# 오른쪽 아래부터 채우기

import sys
input = sys.stdin.readline

g = []
n = int(input())
for _ in range(n):
    g.append(list(map(int, input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        print("i, j:", i, j)
        jump = g[i][j]
        if jump != 0:
            if i + jump < n:
                dp[i + jump][j] += dp[i][j]
            if j + jump < n:
                dp[i][j + jump] += dp[i][j]

print(dp[n-1][n-1])

# for i in range(n-1, -1, -1):
#     for j in range(n-1, -1, -1):
#         jump = g[i][j]
#         if 0 <= i - jump:
#             dp[i][j] += 

