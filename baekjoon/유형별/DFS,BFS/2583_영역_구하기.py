from collections import deque

m, n, k = map(int, input().split())
board = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1

visited = [[False for _ in range(m)] for _ in range(n)]

def bfs(i, j):
    global visited
    area = 1
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        for dx, dy in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
            if 0 <= dx < n and 0 <= dy < m:
                if not visited[dx][dy] and board[dx][dy] == 0:
                    visited[dx][dy] = True
                    area += 1
                    q.append((dx, dy))
    return area

area, cnt = [], 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = True
            if board[i][j] == 0:
                area.append(bfs(i, j))
                cnt += 1

print(cnt)
area.sort()
for a in area:
    print(a, end=' ')