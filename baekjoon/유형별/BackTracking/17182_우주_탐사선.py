import sys
input = sys.stdin.readline

n, K = map(int, input().split())
g = [[0] * n for _ in range(n)]
for i in range(n):
    l = list(map(int, input().split()))
    for j in range(n):
        g[i][j] = l[j]

# 플로이드 워셜
for i in range(n):
    for j in range(n):
        for k in range(n):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])

# 백트래킹
ans = 10000
visited = [False] * n
def find(p, cnt, val):
    global ans, visited
    if cnt == n:
        ans = min(ans, val)
        return
    
    for i in range(n):
        visited[p] = True
        if not visited[i] and i != p:
            find(i, cnt+1, val+g[p][i])
        visited[p] = False
    
find(K, 1, 0)
print(ans)