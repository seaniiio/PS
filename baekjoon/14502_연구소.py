# 0인 것들중에서 벽을 새로 세울 수 있다 → combinations로, 벽을 세울 곳 3개를 구한다
# 벽 3개를 세울 수 있는 모든 경우에 대해, 안전지대의 크기를 구한다 → BFS로
# 안전지대를 구하면 max값인지 확인하고, 모든 경우에 대한 max를 print한다

from collections import deque
import itertools
import copy

n, m = map(int, input().split())
G = []
no_virus = []
is_virus = []
safe_max = 0
for i in range(n):
    G.append(list(map(int, input().split())))
    for j in range(m):
        if G[i][j] == 0:
            no_virus.append([i, j])
        elif G[i][j] == 2:
            is_virus.append([i, j])

def v(new_wall, X, Y):
    new_G = copy.deepcopy(G)
    for wall in new_wall:
        new_G[wall[0]][wall[1]] = 1

    q = deque(is_virus)
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[X][Y] = True
    cnt = 0
    while q:
        x, y = q.popleft()
        for dx, dy in (x+1, y), (x, y+1), (x-1, y), (x, y-1):
            if 0 <= dx < n and 0 <= dy < m and visited[dx][dy] == False and new_G[dx][dy] == 0:
                new_G[dx][dy] = 2
                visited[dx][dy] = True
                q.append([dx, dy])
    for i in range(n):
        for j in range(m):
            if new_G[i][j] == 0:
                cnt += 1
    return cnt

for l in itertools.combinations(no_virus, 3):
    for virus in is_virus:
        safe_max = max(safe_max, v(l, virus[0], virus[1]))

print(safe_max)