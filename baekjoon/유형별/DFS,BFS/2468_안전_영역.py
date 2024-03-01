# bfs
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
G = []
for _ in range(n):
    G.append(list(map(int, input().split())))

def bfs(i, j, visited, k):
    q = deque([[i, j]])
    while q:
        x, y = q.popleft()
        for dx, dy in (x+1, y), (x, y+1), (x-1, y), (x, y-1):
            if 0 <= dx < n and 0 <= dy < n and visited[dx][dy] == False and G[dx][dy] > k:
                visited[dx][dy] = True
                q.append([dx, dy])

ans = 0

for k in range(101):
    cnt = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False and G[i][j] > k:
                visited[i][j] = True
                bfs(i, j, visited, k)
                cnt += 1
    ans = max(ans, cnt)
    if cnt == 0:
        break

print(ans)