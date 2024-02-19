import sys

s1 = [""] + list(sys.stdin.readline().rstrip())
s2 = [""] + list(sys.stdin.readline().rstrip())
dp = [['' for _ in range(len(s1))] for _ in range(len(s2))]

for i in range(1, len(s2)):
    for j in range(1, len(s1)):
        if s1[j] == s2[i]:
            dp[i][j] = dp[i-1][j-1] + s1[j]
        else:
            if len(dp[i][j-1]) <= len(dp[i-1][j]):
                dp[i][j] = dp[i-1][j] 
            else:
                dp[i][j] = dp[i][j-1]
print(len(dp[-1][-1]), dp[-1][-1], sep='\n')