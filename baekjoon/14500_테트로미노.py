import sys

m, n = map(int, input().split())
G = []
for _ in range(m):
    G.append(list(map(int, sys.stdin.readline().split())))

visited = [[False for _ in range(n)] for _ in range(m)]

max_v = 0

def DFS(x, y, cnt, s):
    if cnt == 4:
        global max_v
        max_v = max(max_v, s)
        return
    for dx, dy in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
        if 0 <= dx < m and 0 <= dy < n and visited[dx][dy] == False:
            visited[dx][dy] = True
            DFS(dx, dy, cnt + 1, s + G[dx][dy])
            visited[dx][dy] = False

def F(x, y):
    s1, s2, s3, s4 = 0, 0, 0, 0
    if 0 <= x+2 < m and 0 <= y+1 < n:
        s1 = G[x][y] + G[x+1][y] + G[x+2][y] + G[x+1][y+1]
    if 0 <= x-1 < m and 0 <= y+2 < n:
        s2 = G[x][y] + G[x][y+1] + G[x][y+2] + G[x-1][y+1]
    if 0 <= x-2 < m and 0 <= y-1 < n:
        s3 = G[x][y] + G[x-1][y] + G[x-2][y] + G[x-1][y-1]
    if 0 <= x+1 < m and 0 <= y-2 < n:
        s4 = G[x][y] + G[x][y-1] + G[x][y-2] + G[x+1][y-1]
    
    global max_v
    max_v = max(max_v, s1, s2, s3, s4)

for i in range(m):
    for j in range(n):
        visited[i][j] = True
        DFS(i, j, 1, G[i][j])
        visited[i][j] = False
        F(i, j)

print(max_v)