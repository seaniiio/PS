import sys

n, m = map(int, sys.stdin.readline().split())
result = [0] * 7
nums = [i+1 for i in range(8)]

def DFS(lv):
    if m == lv:
        for i in range(m):
            print(result[i], end=' ')
        print('')
        return
    for i in range(n):
        result[lv] = nums[i]
        DFS(lv + 1)

DFS(0)
    