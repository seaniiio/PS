# 백트래킹
# dfs를 이용하여 순열 print

import sys

n, m = map(int, sys.stdin.readline().split())
nums = [i+1 for i in range(n)]
visited = [False] * 8
result = [0] * 8

def dfs(lv):
    if lv == m:
        for k in range(m):
            print(result[k], end=' ')
        print('')
        return
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            result[lv] = nums[i]
            dfs(lv+1)
            visited[i] = False
        elif visited[i] == True:
            continue
            
dfs(0)