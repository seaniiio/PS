import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
room = []
cctv = []
for i in range(n):
    c = list(map(int, input().split()))
    for j in range(m):
        if 0 < c[j] < 6:
            cctv.append((i, j))
    room.append(c)

cctv_dirs = [[], [(0,), (1,), (2,), (3,)], [(0, 2), (1, 3)], [(3, 0), (0, 1), (1, 2), (2, 3)], [(2, 3, 0), (3, 0, 1), (0, 1, 2), (1, 2, 3)], [(0, 1, 2, 3)]]
dir_xy = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우하좌상

def check(room):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if room[i][j] == 0:
                cnt += 1
    return cnt

ans = n*m

def watch(k, room): # k번째 cctv
    if k >= len(cctv):
        global ans
        ans = min(ans, check(room))
        return
    x, y = cctv[k]
    type = room[x][y]
    for dirs in cctv_dirs[type]:
        this_room = copy.deepcopy(room)
        for dir in dirs:
            dx, dy = dir_xy[dir]
            for i in range(max(n, m)):
                this_x, this_y= x + dx*i, y + dy*i
                if 0 <= this_x < n and 0 <= this_y < m:
                    if this_room[this_x][this_y] == 0:
                        this_room[this_x][this_y] = '#'
                    elif this_room[this_x][this_y] == 6:
                        break
        watch(k+1, this_room)

watch(0, room)
print(ans)