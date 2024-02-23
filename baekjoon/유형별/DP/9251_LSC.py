# LCS

import sys
s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()
l1 = len(s1)
l2 = len(s2)

dp = [[0 for _ in range(len(s1))] for _ in range(len(s2))]

for i in range(len(s1)):
    if s1[i] == s2[0]:
        for j in range(i, len(s1)):
            dp[0][j] = 1

for i in range(len(s2)):
    if s2[i] == s1[0]:
        for j in range(i, len(s2)):
            dp[j][0] = 1

for i in range(1, len(s2)):
    for j in range(1, len(s1)):
        if s2[i] == s1[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(max(dp[-1]))