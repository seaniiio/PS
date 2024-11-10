import sys
from collections import deque
input = sys.stdin.readline

m = []
r, c = map(int, input().split())
for _ in range(r):
    m.append(list(input()))

visited = [[False] * c for _ in range(r)]
total_sheep, total_wolf = 0, 0

def bfs(i, j):
    global visited, total_sheep, total_wolf
    visited[i][j] = True

    if m[i][j] == '#':
        return

    q = deque([])
    sheep, wolf = 0, 0
    q.append((i, j))

    while q:
        x, y = q.popleft()
        visited[x][y] = True
        if m[x][y] == 'v':
            wolf += 1
        elif m[x][y] == 'o':
            sheep += 1
        for dx, dy in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
            if 0 <= dx < r and 0 <= dy < c and visited[dx][dy] == False:
                visited[dx][dy] = True
                if m[dx][dy] != '#':
                    q.append((dx, dy))

    if wolf >= sheep:
        total_wolf += wolf
    else:
        total_sheep += sheep

for i in range(r):
    for j in range(c):
        if visited[i][j] == False:
            bfs(i, j)

print(total_sheep, total_wolf)