# bfs -> 시간초과
# 누적합 구하는 점화식 : G[x2][y2] - G[x1-1][y2] - G[x2][y1-1] + G[x1-1][y1-1] 

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
G = [[0 for _ in range(n+1)]]
for _ in range(n):
    temp = [0]
    temp.extend(list(map(int, input().split())))
    G.append(temp)

for i in range(1, n+1):
    for j in range(1, n+1):
        G[i][j] += (G[i-1][j] + G[i][j-1] - G[i-1][j-1])

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(G[x2][y2] - G[x1-1][y2] - G[x2][y1-1] + G[x1-1][y1-1])


# bfs 풀이
# import sys
# from collections import deque

# input = sys.stdin.readline

# def bfs(x1, y1, x2, y2, G):
#     sum = 0
#     visited = [[False for _ in range(len(G[0]))] for _ in range(len(G))]
#     visited[x1][y1] = True
#     q = deque([[x1, y1]])
#     while q:
#         x, y = q.popleft()
#         sum += G[x][y]
#         for dx, dy in (x+1, y), (x, y+1), (x+1, y+1):
#             if x1 <= dx <= x2 and y1 <= dy <= y2 and visited[dx][dy] == False:
#                 q.append([dx, dy])
#                 visited[dx][dy] = True
#     return sum