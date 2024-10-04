# n=500 -> 250000 -> 모든 정점에 대해 DFS하면 시간초과 -> DP 같이 사용

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
G = []
for _ in range(n):
    G.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
def DFS(i, j):
    global dp
    if dp[i][j] != 0:
        return dp[i][j]
    
    dp[i][j] = 1
    for di, dj in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
        if 0 <= di < n and 0 <= dj < n:
            if G[i][j] < G[di][dj]:
                dp[i][j] = max(dp[i][j], DFS(di, dj) + 1)

    return dp[i][j]

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, DFS(i, j))
print(ans)