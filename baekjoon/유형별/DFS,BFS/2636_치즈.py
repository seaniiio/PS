from collections import deque

n, m = map(int, input().split())
melt_cheese = {i:0 for i in range(1, 101)} # i초에 녹은 치즈 수

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

def find_hole(i, j): # 구멍은 -1처리
    global board, visited_hole

    q = deque([(i, j)])
    holes = [(i, j)]
    is_hole = True

    if not (0 < i < n-1 and 0 < j < m-1):
        is_hole = False

    while q:
        x, y = q.popleft()
        for dx, dy in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
            if 0 <= dx < n and 0 <= dy < m and not visited_hole[dx][dy] and board[dx][dy] == 0:
                visited_hole[dx][dy] = True
                if 0 < dx < n-1 and 0 < dy < m-1:
                    holes.append((dx, dy))
                else:
                    is_hole = False
                q.append((dx, dy))

    if is_hole:
        for x, y in holes:
            board[x][y] = -1

time = 1
visited = [[False for _ in range(m)] for _ in range(n)]
visited_hole = [[False for _ in range(m)] for _ in range(n)]
while True:
    visited_hole = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited_hole[i][j]:
                visited_hole[i][j] = True
                if board[i][j] == 0:
                    find_hole(i, j)

    melt_amount = 0
    to_zero = []
    for i in range(n):
        for j in range(m):
            melt = False
            if board[i][j] == 1:
                for di, dj in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
                    if 0 <= di < n and 0 <= dj < m and board[di][dj] == 0:
                        melt = True
                if melt:
                    visited[i][j] = True
                    to_zero.append((i, j))
                    melt_amount += 1
    if melt_amount == 0:
        break
    for x, y in to_zero:
        board[x][y] = 0
    melt_cheese[time] = melt_amount
    time += 1

    # 구멍 복구
    for x in range(n):
        for y in range(m):
            if board[x][y] == -1:
                board[x][y] = 0
                
print(time-1)
print(melt_cheese[time - 1])