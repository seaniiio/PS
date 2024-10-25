# dp[n][0] : n번이 얼리 어댑터가 아닐 때, n 아래로의 최소 얼리 어댑터 수
# dp[n][1] : n번이 얼리 어댑터일 때, n 아래로의 최소 얼리 어댑터 수
# dp[n][0] = 자식들의 dp[][1] 합
# dp[n][1] = 자식들의 min(dp[]) 합

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n = int(input())
graph = {i : [] for i in range(1, n+1)}
for _ in range(n-1):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)

dp = [[0, 0] for _ in range(n+1)]
visited = [False] * (n+1)

def dfs(v):
    global dp, visited
    early_sum, min_sum = 0, 0
    visited[v] = True
    for d in graph[v]:
        if visited[d] == False:
            dfs(d)
        early_sum += dp[d][1]
        min_sum += min(dp[d])

    dp[v] = [early_sum, min_sum + 1]

dfs(1)
print(min(dp[1]))

