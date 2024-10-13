from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)

n = int(input())
g = []
for _ in range(n):
    g.append(list(map(int, input().split())))
ans = [[0] * (n) for _ in range(n)]

dir_next = [(0, 2), (1, 2), (0, 1, 2)]
dir_next_dir = [[(0, 1)], [(1, 0)], [(1, 1), (0, 1), (1, 0)]]
visited = {}

# DFS
stk = [[[0, 1], 0, 1]]

def DFS(x, y, dir):
    cnt = 0
    if (x, y, dir) in visited:
        return visited[(x, y, dir)]
    
    if x == n-1 and y == n-1:
        return 1

    for next_dir in dir_next[dir]:
        p = True
        for dx, dy in dir_next_dir[next_dir]:
            nextX, nextY = x + dx, y + dy
            if 0 <= nextX < n and 0 <= nextY < n and g[nextX][nextY] != 1:
                continue
            else:
                p = False
                break
        if p:
            cnt += DFS(x + dir_next_dir[next_dir][0][0], y + dir_next_dir[next_dir][0][1], next_dir)

    visited[(x, y, dir)] = cnt
    return cnt

print(DFS(0, 1, 0))


# BFS -> 시간 초과
# n = int(input())
# g = []
# for _ in range(n):
#     g.append(list(map(int, input().split())))
# ans = [[0] * (n) for _ in range(n)]

# dir_next = [(0, 2), (1, 2), (0, 1, 2)]
# dir_next_dir = [[(0, 1)], [(1, 0)], [(1, 1), (0, 1), (1, 0)]]
# q = deque([[[0, 1], 0, 1]])

# while q:
#     now, now_dir, cnt = q.popleft()
#     ans[now[0]][now[1]] += cnt
#     for next_dir in dir_next[now_dir]:
#         p = True
#         for dx, dy in dir_next_dir[next_dir]: # 갈 수 있는지 검사
#             nextX, nextY = now[0] + dx, now[1] + dy
#             if 0 <= nextX < n and 0 <= nextY < n and g[nextX][nextY] != 1:
#                 continue
#             else:
#                 p = False
#                 break
#         if p:
#             q.append([[now[0] + dir_next_dir[next_dir][0][0], now[1] + dir_next_dir[next_dir][0][1]], next_dir, cnt])

# print(ans[n-1][n-1])