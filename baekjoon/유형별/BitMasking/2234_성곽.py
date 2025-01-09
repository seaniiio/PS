import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
can_go = {} # 갈 수 있는 경로 저장
go_dir = {0 : (0, -1), 1: (-1, 0), 2: (0, 1), 3: (1, 0)} # 0:서 1:북 2:동 3:남

# Bitmask
for i in range(m):
    l = list(map(int, input().split()))
    for j in range(n):
        bin_s = bin(l[j])[2:]
        while len(bin_s) != 4:
            bin_s = "0" + bin_s
        no_wall = []
        for k in range(len(bin_s)):
            if bin_s[len(bin_s) - 1 - k] == '0':
                no_wall.append(k)
        
        can_go[(i, j)] = no_wall

# BFS
next_room_num = 1
room_num = [[0] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]
room_size = {}

def BFS(x, y):
    global visited
    cnt = 0
    deq = deque([(x, y)])
    while deq:
        nx, ny = deq.popleft()
        room_num[nx][ny] = next_room_num
        cnt += 1
        for dir in range(4):
            for dir in can_go[(nx, ny)]: # 갈 수 있는 경우
                dx, dy = nx + go_dir[dir][0], ny + go_dir[dir][1]
                if (0 <= dx < m) and (0 <= dy < n) and not visited[dx][dy]:
                    visited[dx][dy] = True
                    deq.append((dx, dy))
                
    room_size[next_room_num] = cnt

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            BFS(i, j)
            next_room_num += 1

print(next_room_num - 1)
print(max(room_size.values()))

sum_max = 0
for i in range(m):
    for j in range(n):
        for nx, ny in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            if 0 <= nx < m and 0 <= ny < n and room_num[nx][ny] != room_num[i][j]:
                sum_max = max(sum_max, room_size[room_num[nx][ny]] + room_size[room_num[i][j]])
print(sum_max)