import sys
from collections import deque

m, n, h = map(int, input().split())
G = []
for _ in range(h):
    t = []
    for _ in range(n):
        t.append(list(map(int, sys.stdin.readline().split())))
    G.append(t)

visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
q = deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if G[i][j][k] == 1:
                q.append([i, j, k, 0])
                visited[i][j][k] = True

answer = 0

while q:
    x, y, z, cnt = q.popleft()
    for dx, dy, dz in (x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1):
        if 0 <= dx < h and 0 <= dy < n and 0 <= dz < m and visited[dx][dy][dz] == False and G[dx][dy][dz] == 0:
            q.append([dx, dy, dz, cnt + 1])
            visited[dx][dy][dz] = True
            answer = max(answer, cnt + 1)
            G[dx][dy][dz] = 1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if G[i][j][k] == 0:
                answer = -1

print(answer)