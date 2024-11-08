import sys
import math
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
balls = deque([])
for _ in range(M):
    x, y, m, s, d = map(int, input().split())
    balls.append((x-1, y-1, m, s, d))

def move():
    # 이동
    global balls
    board = [[[] for _ in range(N)] for _ in range(N)]
    new_balls = []
    while balls:
        x, y, m, s, d = balls.popleft()
        dx, dy = get_dest(x, y, d, s)
        new_balls.append((dx, dy, m, s, d))
        board[dx][dy].append((m, s, d))
    
    new_new_balls = deque([])
    # 2개 이상 있으면 분열
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) < 1:
                continue
            elif len(board[i][j]) == 1:
                new_new_balls.append((i, j, board[i][j][0][0], board[i][j][0][1], board[i][j][0][2]))
                continue
            # 분열
            count = len(board[i][j])
            m_sum, s_sum = 0, 0
            dir_one = board[i][j][0][2] % 2
            dirs = [0, 2, 4, 6]
            for ball in board[i][j][:]:
                b_m, b_s, b_d = ball
                m_sum += b_m
                s_sum += b_s
                if b_d % 2 != dir_one:
                    dirs = [1, 3, 5, 7]

            if m_sum // 5 > 0:
                for n in range(4):
                    new_new_balls.append((i, j, math.floor(m_sum / 5), math.floor(s_sum / count), dirs[n]))

    balls = new_new_balls

def get_dest(x, y, d, s):
    dir = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    new_s = s % N
    dx = x + dir[d][0] * new_s
    dy = y + dir[d][1] * new_s

    if dx < 0:
        dx = N + dx
    elif dx >= N:
        dx %= N
    if dy < 0:
        dy = N + dy
    elif dy >= N:
        dy %= N

    return (dx, dy)

for _ in range(K):
    move()

ans = 0
for b in balls:
    ans += b[2]

print(ans)