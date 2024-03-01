from collections import deque
import sys
m, n = map(int, sys.stdin.readline().split())
G = []
for _ in range(n):
    G.append(list(sys.stdin.readline().rstrip()))
visited = [[False for _ in range(m)] for _ in range(n)]

def dfs(i, j):
    global visited
    cnt = 0
    color = G[i][j]
    q = deque([[i, j, 1]])

    while q:
        cnt += 1
        x, y, c = q.popleft()
        for dx, dy in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if 0 <= dx < n and 0 <= dy < m and visited[dx][dy] == False and G[dx][dy] == color:
                visited[dx][dy] = True
                q.append([dx, dy, c+1])
    return color, cnt


result = {'W' : 0, 'B' : 0}
for i in range(n):
    for j in range(m):
        if visited[i][j] == False:
            visited[i][j] = True
            c, r = dfs(i, j)
            result[c] += r ** 2

print(result['W'], result['B'])