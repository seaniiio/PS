import sys
from collections import deque

m, n = map(int, input().split())
G = []
dist = [[-1 for _ in range(n)] for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]
x, y = 0, 0

for i in range(m):
    l = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if l[j] == 2:
            x, y = i, j
    G.append(l)

def Find(x, y, cnt):
    q = deque([[x, y, cnt]])
    while q:
        v = q.popleft()
        x, y, cnt = v[0], v[1], v[2]
        for dx, dy in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if 0 <= dx < m and 0 <= dy < n:
                if G[dx][dy] == 1 and visited[dx][dy] == False:
                    visited[dx][dy] = True
                    dist[dx][dy] = cnt
                    q.append([dx, dy, cnt + 1])

dist[x][y] = 0
visited[x][y] = True
Find(x, y, 1)

for i in range(m):
    for j in range(n):
        if G[i][j] == 0:
            dist[i][j] = 0

for i in range(m):
    for j in range(n):
        print(dist[i][j], end=' ')
    print()