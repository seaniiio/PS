import sys

n, m = map(int, sys.stdin.readline().split())
result = [0] * 8
visited = [False] * 8
nums = [i+1 for i in range(n)]

def DFS(lv):
    if lv == m:
        for i in range(m):
            print(result[i], end=' ')
        print('')
        return
    for i in range(n):
        if visited[i] == False:
            if lv == 0:
                visited[i] = True
                result[lv] = nums[i]
                DFS(lv+1)
                visited[i] = False
            elif lv >= 1 and result[lv - 1] < nums[i]:
                visited[i] = True
                result[lv] = nums[i]
                DFS(lv+1)
                visited[i] = False
            
        elif visited[i] == True:
            continue

DFS(0)