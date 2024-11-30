# 외부 공기 찾기 <-> 녹는 치즈 찾기 반복
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())
g = []
for _ in range(n):
    g.append(list(map(int, input().split())))

# 공기 찾기
def find_air(i, j, air_visited):
    global g
    if g[i][j] != 1: # 공기인 경우
        g[i][j] = -1
        for di, dj in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            if 0 <= di < n and 0 <= dj < m and not air_visited[di][dj]:
                air_visited[di][dj] = True
                find_air(di, dj, air_visited)
    
def cheese_melt(i, j):
    cnt = 0
    for di, dj in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
        if 0 <= di < n and 0 <= dj < m and g[di][dj] == -1:
            cnt += 1

    return (cnt >= 2)

ans = 0

while True:
    total_cheese = []

    air_visited = [[False] * m for _ in range(n)]
    air_visited[0][0] = True
    find_air(0, 0, air_visited)

    cheese_visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                if cheese_melt(i, j):
                    total_cheese.append((i, j))
    
    for mi, mj in total_cheese:
        g[mi][mj] = -1

    if len(total_cheese) == 0:
        break

    ans += 1

print(ans)