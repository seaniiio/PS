import sys
from collections import deque

m, n = map(int, input().split())
G = []
for _ in range(n):
    G.append(list(map(int, sys.stdin.readline().split())))

visit = [[False for _ in range(m)] for _ in range(n)]
q = deque([])

for i in range(n):
    for j in range(m):
        if G[i][j] == 1:
            q.append([i, j, 0])
            visit[i][j] = True

Dx = [1, -1, 0, 0]
Dy = [0, 0, 1, -1]
answer = 0

while q:
    x, y, day = q.popleft()
    answer = max(answer, day)
    for dx, dy in zip(Dx, Dy):
        X, Y = x + dx, y + dy
        if 0 <= X < n and 0 <= Y < m:
            if G[X][Y] == 0 and visit[X][Y] == False:
                visit[X][Y] = True
                G[X][Y] = 1
                q.append([X, Y, day + 1])

for i in range(n):
    if 0 in G[i]:
        answer = -1

print(answer)