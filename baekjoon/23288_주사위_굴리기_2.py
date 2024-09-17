from collections import deque

n, m, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dice = [0, 1, 2, 3, 4, 5, 6]
dir_dx = [0, 1, 0, -1]
dir_dy = [1, 0, -1, 0]
reverse_dir = {0:2, 1:3, 2:0, 3:1}
dir = 0 # 동쪽
x, y = 0, 0
floor = 6 # 주사위 밑면

def roll(dir):
    global dice
    if dir == 0: # 동
        dice = [0, dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]]
    elif dir == 1: # 남
        dice = [0, dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]]
    elif dir == 2: # 서
        dice = [0, dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]]
    elif dir == 3 : # 북
        dice = [0, dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]]
    return dice[6]

def bfs(i, j, k):
    cnt = 0
    q = deque([[i, j]])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        cnt += k
        for dx, dy in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if 0 <= dx < n and 0 <= dy < m:
                if visited[dx][dy] == False and board[dx][dy] == k:
                    q.append([dx, dy])
                    visited[dx][dy] = True
    return cnt

score = 0
for _ in range(k):
    if (not 0 <= x + dir_dx[dir] < n) or (not 0 <= y + dir_dy[dir] < m): # 반대방향으로
        dir = reverse_dir[dir]

    x, y = x + dir_dx[dir], y + dir_dy[dir] # 이동
    floor = roll(dir)
    if floor > board[x][y]:
        dir = dir+1 if dir < 3 else 0
    elif floor < board[x][y]:
        dir = dir-1 if dir > 0 else 3

    #점수 계산
    score += bfs(x, y, board[x][y])

print(score)