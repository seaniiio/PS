import sys
import copy
sys.setrecursionlimit(10 ** 6)

g = [[[0, 0]] * 4 for _ in range(4)] # 번호, 방향
for i in range(4):
    l = list(map(int, input().split()))
    for j in range(4):
        g[i][j] = [l[j*2], l[j*2+1]-1]

shark = [0, 0, 0] # x, y, 방향
dir = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
answer = 0

def eat(x, y, g, score):
    global answer
    temp_g = copy.deepcopy(g)

    # 상어 먹기
    eat_fish, shark_next_dir = temp_g[x][y]
    score += eat_fish
    temp_g[x][y] = [0, shark_next_dir]
    answer = max(answer, score)
    
    # 물고기 이동
    for k in range(1, 17):
        f_x, f_y = -1, -1
        for i in range(4):
            for j in range(4):
                if temp_g[i][j][0] == k:
                    f_x, f_y = i, j
                    break
        if f_x == -1 and f_y == -1:
            continue

        now_dir = temp_g[f_x][f_y][1]
        for i in range(8):
            next_dir = (now_dir + i) % 8
            next_x, next_y = f_x + dir[next_dir][0], f_y + dir[next_dir][1]
            if not (0 <= next_x < 4 and 0 <= next_y < 4) or (next_x == x and next_y == y):
                continue
            temp_g[f_x][f_y][1] = next_dir
            temp_g[next_x][next_y], temp_g[f_x][f_y] = temp_g[f_x][f_y], temp_g[next_x][next_y]
            break
    
    # 상어 이동
    for k in range(1, 4):
        n_x, n_y = x + dir[shark_next_dir][0] * k, y + dir[shark_next_dir][1] * k
        if 0 <= n_x < 4 and 0 <= n_y < 4 and temp_g[n_x][n_y][0] > 0:
            eat(n_x, n_y, temp_g, score)

eat(0, 0, g, 0)
print(answer)