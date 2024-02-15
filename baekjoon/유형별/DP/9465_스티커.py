import sys

t = int(input())
for _ in range(t):
    G = []
    n = int(input())
    for _ in range(2):
        G.append(list(map(int, sys.stdin.readline().split()))) 
    dp = [[0, 0] for _ in range(n)]
    dp[0] = [G[0][0], G[1][0]]
    if n > 1:
        dp[1] = [G[1][0] + G[0][1], G[0][0] + G[1][1]]

    for i in range(2, n):
        dp[i][0] = max(max(dp[i-2]) + G[0][i], dp[i-1][1] + G[0][i])
        dp[i][1] = max(max(dp[i-2]) + G[1][i], dp[i-1][0] + G[1][i])
    print(max(dp[n-1]))
