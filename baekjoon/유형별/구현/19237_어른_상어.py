import sys
input = sys.stdin.readline

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우
N, M, K = map(int, input().split())
board = [[[0, 0, 0]] * N for _ in range(N)] # 현재 상어, 냄새남긴 상어, 냄새 남은시간
sharks = {i : [] for i in range(1, M+1)} # 행, 열, 방향
sharks_dir = {i : [] for i in range(1, M+1)} # 각 상어의 방향 우선순위

for i in range(N):
    l = list(map(int, input().split()))
    for j in range(N):
        if l[j] != 0:
            board[i][j] = [l[j], 0, 0]
            sharks[l[j]] = [i, j, 0]

l = list(map(int, input().split()))
for i in range(M): # 상어 방향
    sharks[i+1][2] = l[i] - 1

for i in range(M): # 상어 방향 우선순위
    for _ in range(4):
        sharks_dir[i+1].append(list(map(lambda x : x-1, map(int, input().split()))))

time = 0
while True:
    time += 1
    if time == 1001:
        time = -1
        break

    # 냄새 뿌리기
    for i in range(1, M+1):
        s_x, s_y = sharks[i][0], sharks[i][1]
        if (s_x, s_y) != (-1, -1):
            board[s_x][s_y][1] = i
            board[s_x][s_y][2] = K

    # 상어 이동
    for s in range(1, M+1):
        s_x, s_y, s_d = sharks[s]

        move = False
        # 먼저 냄새 없는 곳 찾음
        for n_d in sharks_dir[s][s_d]:
            n_x, n_y = s_x + dir[n_d][0], s_y + dir[n_d][1]
            if not (0 <= n_x < N and 0 <= n_y < N) or board[n_x][n_y][1] != 0: # 갈 수 없음
                continue
            elif board[n_x][n_y][0] != 0: # 이미 상어 있음 -> 먹힘
                sharks[s] = [-1, -1, -1]
                board[s_x][s_y][0] = 0
                move = True
                break
            else: # 갈 수 있음
                board[n_x][n_y] = [s, 0, 0]
                sharks[s] = [n_x, n_y, n_d]
                board[s_x][s_y][0] = 0
                move = True
                break
        
        if not move:
            # 냄새 없는 곳이 없으면 내 냄새 찾아감
            for n_d in sharks_dir[s][s_d]:
                n_x, n_y = s_x + dir[n_d][0], s_y + dir[n_d][1]
                if not (0 <= n_x < N and 0 <= n_y < N) or board[n_x][n_y][1] != s: # 갈 수 없음
                    continue
                if board[n_x][n_y][1] == s:
                    if board[n_x][n_y][0] != 0: # 이미 상어 있음 -> 먹힘
                        sharks[s] = [-1, -1, -1]
                        board[s_x][s_y][0] = 0
                        break
                    else: # 갈 수 있음
                        board[n_x][n_y] = [s, s, K]
                        sharks[s] = [n_x, n_y, n_d]
                        board[s_x][s_y][0] = 0
                        break

    # 냄새 1 지우기
    for i in range(N):
        for j in range(N):
            if board[i][j][2] > 1:
                board[i][j][2] -= 1
            elif board[i][j][2] == 1:
                board[i][j][1], board[i][j][2] = 0, 0

    # 1만 남았는지 검사
    left = 0
    for s in range(2, M+1):
        if sharks[s] != [-1, -1, -1]:
            left += 1
    if left == 0:
        break

print(time)