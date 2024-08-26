r, c, t = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(map(int, input().split())))

clean_1, clean_2 = 0, 0
for r_i in range(r):
    if board[r_i][0] == -1:
        clean_1, clean_2 = r_i, r_i+1
        break

for _ in range(t):
    # 확산
    change = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                m_amount = board[i][j] // 5
                m_cnt = 0
                for di, dj in (i+1, j), (i-1, j), (i, j-1), (i, j+1):
                    if 0 <= di < r and 0 <= dj < c:
                        if di in (clean_1, clean_2) and dj == 0:
                            continue
                        m_cnt += 1
                        change[di][dj] += m_amount
                change[i][j] -= (m_amount * m_cnt)

    for i in range(r):
        for j in range(c):
            board[i][j] += change[i][j]
    # 청정
    board[clean_1][0], board[clean_2][0] = 0, 0

    for row_0 in range(clean_1-1, -1, -1):
        board[row_0+1][0] = board[row_0][0]
    for row_0 in range(clean_2+1, r):
        board[row_0-1][0] = board[row_0][0]

    for col_0 in range(1, c):
        board[0][col_0-1] = board[0][col_0]
        board[r-1][col_0-1] = board[r-1][col_0]
    
    for row_r in range(1, clean_1+1):
        board[row_r-1][c-1] = board[row_r][c-1]
    for row_r in range(r-2, clean_2-1, -1):
        board[row_r+1][c-1] = board[row_r][c-1]
    
    board[clean_1][0], board[clean_2][0] = 0, 0
    for col_c in range(c-2, -1, -1):
        board[clean_1][col_c+1] = board[clean_1][col_c]
        board[clean_2][col_c+1] = board[clean_2][col_c]

    board[clean_1][0], board[clean_2][0] = 0, 0 

total = 0
for i in range(r):
    for j in range(c):
        total += board[i][j]
print(total)