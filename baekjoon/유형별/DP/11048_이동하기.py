import sys

n, m = map(int, sys.stdin.readline().split())
l, room = [], [] # m x n
for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))
for i in range(m):
    room.append(list(l[j][i] for j in range(n)))

d = [[1, 0], [0, 1], [1, 1]]
for i in range(m):
    for j in range(n):
        max = 0
        for dx, dy in d:
            x, y = i - dx, j - dy
            if 0 <= x < m and 0 <= y < n:
                if room[x][y] > max: max = room[x][y]
        room[i][j] += max

print(room[m-1][n-1])