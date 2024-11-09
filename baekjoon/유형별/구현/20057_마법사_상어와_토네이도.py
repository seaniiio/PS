import sys
import math
input = sys.stdin.readline

n = int(input())
b = []

for _ in range(n):
    b.append(list(map(int, input().split())))

t_x, t_y = n // 2, n // 2
t_d = 0
d = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def rotate(l):
    return list(reversed(list(zip(*l))))

per_0 = [[0, 0, 0.02, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0.05, 0, 0, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0, 0, 0.02, 0, 0]]
per_1 = rotate(per_0)
per_2 = rotate(per_1)
per_3 = rotate(per_2)
per = [per_0, per_1, per_2, per_3]

change_threshold, change_cnt = 1, 0
dir_threshold = 0
ans = 0
while True:
    if t_x == 0 and t_y == 0:
        break

    # 토네이도 이동
    t_x += d[t_d][0]
    t_y += d[t_d][1]
    
    change_cnt += 1

    # 모래 이동
    sand = b[t_x][t_y]
    b[t_x][t_y] = 0
    left_sands = sand

    for i in range(5):
        for j in range(5):
            move_sand = math.floor(sand * per[t_d][i][j])
            left_sands -= move_sand
            if 0 <= t_x + i - 2 < n and 0 <= t_y + j - 2 < n:
                b[t_x+i-2][t_y+j-2] += move_sand
            else:
                ans += move_sand

    a_x, a_y = t_x + d[t_d][0], t_y + d[t_d][1]
    if 0 <= a_x < n and 0 <= a_y < n:
        b[a_x][a_y] += left_sands
    else:
        ans += left_sands
    
    if (change_threshold == change_cnt):
        # 방향 바꾸기
        dir_threshold += 1 # 방향 바꾼게 2번 -> change_threshold += 1
        if dir_threshold == 2:
            change_threshold += 1
            dir_threshold = 0
        
        change_cnt = 0
        t_d = t_d + 1 if t_d < 3 else 0

print(ans)