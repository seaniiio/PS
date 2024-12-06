# dp[n] = dp[n-1] 전부 + dp[n-2]에서 2,3만 있는거 + dp[n-3]에서 3만 있는거

import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

t = int(input())
dp = {i : [0, 0, 0] for i in range(1, 10001)} # [0, 0, 0] : 전체, 2,3 있는거, 3만 있는거

dp[1] = [1, 0, 0]
dp[2] = [2, 1, 0]
dp[3] = [3, 0, 1]
visited = {i : False for i in range(1, 10001)}
visited[1] = visited[2] = visited[3] = True

def find(k):
    global dp
    if visited[k]:
        return
    if visited[k-1] == False:
        find(k-1)
    dp[k][0] = dp[k-1][0] + dp[k-2][1] + dp[k-2][2] + dp[k-3][2]
    dp[k][1] = dp[k-2][1] + dp[k-2][2]
    dp[k][2] = dp[k-3][2]

    visited[k] = True

for _ in range(t):
    k = int(input())
    find(k)
    print(dp[k][0])
    
