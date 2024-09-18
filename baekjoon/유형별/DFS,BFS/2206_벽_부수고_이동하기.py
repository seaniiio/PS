# BFS인데, 벽 부순 여부 저장
# 현재까지 벽을 안 부수고 이동했는지, 벽을 하나 부수고 이동했는지에 대해 따로 최소거리 저장
# visited[벽 안부쉈을 때 최소경로, 벽 부쉈을때 최소 경로]
# 이렇게 따로 관리해야 함

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
g = []
for _ in range(n):
    g.append(list(map(int, list(input().strip()))))

q = deque([[0, 0, 1, False]])
visited = [[[1000001, 1000001] for _ in range(m)] for _ in range(n)]
visited[0][0] = [1, 1]
while q:
    x, y, d, w = q.popleft()
    for dx, dy in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
        if 0 <= dx < n and 0 <= dy < m:
            if w == False and g[dx][dy] == 0 and visited[dx][dy][0] > d+1: # 벽 안부수고 이동한 최소 거리
                visited[dx][dy][0] = d+1
                q.append([dx, dy, d+1, False])
            elif w == True and g[dx][dy] == 0 and visited[dx][dy][1] > d+1: # 벽 부수고 이동한 최소 거리
                visited[dx][dy][1] = d+1
                q.append([dx, dy, d+1, True])
            elif w == False and g[dx][dy] == 1 and visited[dx][dy][1] > d+1: # 여기서 벽 부순 경우
                visited[dx][dy][1] = d+1
                q.append([dx, dy, d+1, True])

ans = min(visited[n-1][m-1])
if ans == 1000001:
    ans = -1
print(ans)