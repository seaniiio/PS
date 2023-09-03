import sys

n, m = map(int, sys.stdin.readline().split())
visited = [False] * 8
nums = [i+1 for i in range(8)]
result = [0] * 8

def DFS(lv):
    if lv == m:
        for i in range(m):
            print(result[i], end=' ')
        print('')
        return
    for i in range(n):
        if visited[i] == True:
            continue
        for j in range(i):
            visited[j] = True
        result[lv] = nums[i]
        DFS(lv + 1)
        for j in range(i):
            visited[j] = False
        
DFS(0)