import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
G = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    G[x-1][y-1] = 1

cnt = 0

def bfs(i, j, visited):
    global cnt
    q = deque([[i, j]])
    cnt_now = 1
    while q:
        x, y = q.popleft()
        for dx, dy in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if 0 <= dx < n and 0 <= dy < m and G[dx][dy] == 1 and visited[dx][dy] == False:
                visited[dx][dy] = True
                cnt_now += 1
                q.append([dx, dy])
    cnt = max(cnt, cnt_now)

for i in range(n):
    for j in range(m):
        if G[i][j] == 1 and visited[i][j] == False:
            visited[i][j] = True
            bfs(i, j, visited)

print(cnt)
