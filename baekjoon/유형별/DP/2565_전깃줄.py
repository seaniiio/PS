# LIS : 가장 긴 증가하는 부분수열

import sys
n = int(input())
G = []
for _ in range(n):
    G.append(list(map(int, sys.stdin.readline().split())))
G.sort(key = lambda x : x[0])

dp = [1 for _ in range(len(G))]
for i in range(1, len(G)):
    for j in range(i):
        if G[i][1] > G[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(n - max(dp))