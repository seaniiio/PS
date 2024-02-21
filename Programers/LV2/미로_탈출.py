from collections import deque

def BFS(startX, startY, endX, endY, G):
    q = deque([[startX, startY, 0]])
    visited = [[False for _ in range(len(G[0]))] for _ in range(len(G))]
    visited[startX][startY] = True
    while q:
        x, y, t = q.popleft()
        if x == endX and y == endY:
            return t
        for dx, dy in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if 0 <= dx < len(G) and 0 <= dy < len(G[0]) and G[dx][dy] != 'X' and visited[dx][dy] == False:
                visited[dx][dy] = True
                q.append([dx, dy, t+1])
    return -1

def solution(maps):
    s_x, s_y, l_x, l_y, e_x, e_y = 0, 0, 0, 0, 0, 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                s_x, s_y = i, j
            if maps[i][j] == 'L':
                l_x, l_y = i, j
            if maps[i][j] == 'E':
                e_x, e_y = i, j  
    to_l = BFS(s_x, s_y, l_x, l_y, maps)
    to_e = BFS(l_x, l_y, e_x, e_y, maps)
    if to_l == -1 or to_e == -1:
        return -1
    return to_l + to_e