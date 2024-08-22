# n = 50
# 왼쪽 위에서부터 비교
# 한 칸에서 DFS -> 연합 찾기

N, L, R = map(int, input().split())
land = []
for _ in range(N):
    land.append(list(map(int, input().split())))

total_day = 0

def DFS(x, y):
    stk = [(x, y)]
    unions = [(x, y)]
    global union_exist
    global land
    global visited
    while len(stk) != 0:
        x, y = stk.pop()
        visited[x][y] = True
        for dx, dy in (x, y+1), (x+1, y), (x-1, y), (x, y-1):
            if 0 <= dx < N and 0 <= dy < N:
                if (visited[dx][dy] == False) and (L <= abs(land[x][y] - land[dx][dy]) <= R):
                    visited[dx][dy] = True # 이거 빼면 틀림
                    stk.append((dx, dy))
                    unions.append((dx, dy))
                    union_exist = True

    populations = 0
    for u_x, u_y in unions:
        populations += land[u_x][u_y]
    
    populations //= len(unions)
    for u_x, u_y in unions:
        land[u_x][u_y] = populations
    return

union_exist = True
while True:
    # DFS
    global visited
    visited = [[False for _ in range(N)] for _ in range(N)]
    union_exist = False
    for j in range(N):
        for i in range(N):
            if visited[i][j] == False:
                DFS(i, j)

    if union_exist:
        total_day += 1
    else:
        break

print(total_day)
