# 보드판 크기가 100*100, 시도횟수가 100 -> 완전탐색해도 충분
from collections import deque

n = int(input())
k = int(input())
board = [['x' for _ in range(n)] for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 'a'

change = []
L = int(input())
for _ in range(L):
    t, d = input().split()
    change.append([int(t), d])

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

x, y = 0, 0
snakes = deque([[0, 0]])
change_idx = 0
total_time = 0
now_dir = 0
while True:
    if change_idx < L and change[change_idx][0] == total_time:
        if change[change_idx][1] == 'D':
            now_dir = now_dir + 1 if now_dir < 3 else 0
        elif change[change_idx][1] == 'L':
            now_dir = now_dir - 1 if now_dir > 0 else 3
        change_idx += 1
    
    next_x = x + dx[now_dir]
    next_y = y + dy[now_dir]
    if 0 <= next_x < n and 0 <= next_y < n:
        if [next_x, next_y] in snakes:
            break
        elif board[next_x][next_y] == 'a':
            board[next_x][next_y] = 'x'
        elif board[next_x][next_y] == 'x':
            snakes.popleft()
        snakes.append([next_x, next_y])
        x, y = next_x, next_y
    else:
        break
    total_time += 1

print(total_time + 1)