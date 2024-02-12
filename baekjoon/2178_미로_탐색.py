import sys
from collections import deque

n, m = map(int, input().split())
G = []
for _ in range(n):
    G.append(list(sys.stdin.readline()))

def BFS(X, Y):
    q = deque([[X, Y, 0]])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    while q:
        x, y, c = q.popleft()
        if x == n-1 and y == m-1:
            return c + 1
        for dx, dy in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if 0 <= dx < n and 0 <= dy < m and visited[dx][dy] == False and G[dx][dy] == '1':
                visited[dx][dy] = True
                q.append([dx, dy, c+1])

print(BFS(0, 0))