import sys

n, m = map(int, input().split())
x, y, dir = map(int, input().split())
G = []
visited = [[False for _ in range(m)] for _ in range(n)]
answer = 0
for _ in range(n):
    G.append(list(map(int, sys.stdin.readline().split())))

# 반시계 회전
def cir(k):
    return 3 if k == 0 else k-1

d = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def DFS(x, y, dir):
    global answer
    if G[x][y] == 0:
        G[x][y] = 2
        answer += 1
    exist = False
    for nx, ny in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
        if 0 <= nx < n and 0 <= ny < m and G[nx][ny] == 0:
            exist = True
    if exist: # 청소안된칸 있으면
        while True:
            dir = cir(dir)
            dx, dy = x + d[dir][0], y + d[dir][1]
            if 0 <= dx < n and 0 <= dy < m and G[dx][dy] == 0: # 앞칸 청소 x
                DFS(dx, dy, dir)
                break
    elif not exist: # 모두 청소되어있으면
        dx, dy = x - d[dir][0], y - d[dir][1]
        if 0 <= dx < n and 0 <= dy < m and G[dx][dy] != 1: # 후진 o
            DFS(dx, dy, dir)
        else:
            return

DFS(x, y, dir)
print(answer)