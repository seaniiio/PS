import sys
from collections import deque

G = []
n = int(input())
for _ in range(n):
    G.append(list(sys.stdin.readline()))

global visited_x, visited_o
visited_x, visited_o = [[False for _ in range(n)] for _ in range(n)] * n, [[False for _ in range(n)] for _ in range(n)]

def BFS_X(X, Y, C):
    q = deque([[X, Y]])
    while q:
        x, y = q.popleft()
        for dx, dy in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if 0 <= dx < n and 0 <= dy < n:
                if visited_x[dx][dy] == False and G[dx][dy] == C:
                    visited_x[dx][dy] = True
                    q.append([dx, dy])

def BFS_O(X, Y, C):
    c = False
    if C == 'R' or C == 'G':
        c = True
    q = deque([[X, Y]])
    while q:
        x, y = q.popleft()
        for dx, dy in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if 0 <= dx < n and 0 <= dy < n:
                if c: # G or R
                    if visited_o[dx][dy] == False and G[dx][dy] != 'B':
                        visited_o[dx][dy] = True
                        q.append([dx, dy])
                else: # B
                    if visited_o[dx][dy] == False and G[dx][dy] == 'B':
                        visited_o[dx][dy] = True
                        q.append([dx, dy])

cnt_x, cnt_o = 0, 0

for i in range(n):
    for j in range(n):
        if visited_x[i][j] == False:
            visited_x[i][j] = True
            cnt_x += 1
            BFS_X(i, j, G[i][j])

for i in range(n):
    for j in range(n):
        if visited_o[i][j] == False:
            visited_o[i][j] = True
            cnt_o += 1
            BFS_O(i, j, G[i][j])

print(cnt_x, cnt_o)