import sys
from collections import deque

n, m = map(int, input().split())
G = []
x, y = 0, 0
for i in range(n):
    G.append(list(sys.stdin.readline()))
    for j in range(m):
        if G[i][j] =='I':
            x, y = i, j
visited = [[False for _ in range(m)] for _ in range(n)]

def BFS(X, Y):
    person = 0
    q = deque([[X, Y]])
    while q:
        x, y = q.popleft()
        for dx, dy in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if 0 <= dx < n and 0 <= dy < m and visited[dx][dy] == False:
                visited[dx][dy] = True
                if G[dx][dy] == 'O':
                    q.append([dx, dy])
                elif G[dx][dy] == 'P':
                    person += 1
                    q.append([dx, dy])
    return person

visited[x][y] = True
person = BFS(x, y)
if person == 0:
    print('TT')
else:
    print(person)