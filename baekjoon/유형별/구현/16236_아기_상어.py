# BFS에서, 탐색 순서로 무조건 최적의 물고기를 찾을 수 있는게 아님 -> 거리가 같은 물고기들을 우선순위큐로 비교(행 작은 순서 -> 열 작은 순서)

from collections import deque
import heapq

n = int(input())
board = []
x, y = 0, 0
size = 2
fish_ate = 0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 9:
            x, y = i, j
    board.append(row)

total_time = 0

while True:
    fish = deque([(x, y, 1)])
    board[x][y] = 0
    min_time_fish = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[x][y] = True
    find = False
    min_time = 400
    while len(fish) != 0:
        now_x, now_y, time = fish.popleft()
        if time <= min_time:
            for i in range(4):
                next_x, next_y = now_x + dx[i], now_y + dy[i]
                if 0 <= next_x < n and 0 <= next_y < n:
                    if 1 <= board[next_x][next_y] < size:
                        if time <= min_time:
                            min_time = time
                            heapq.heappush(min_time_fish, (next_x, next_y))

                        break
                    elif board[next_x][next_y] <= size and visited[next_x][next_y] == False:
                        visited[next_x][next_y] = True
                        fish.append((next_x, next_y, time+1))

    if len(min_time_fish) != 0: # 처음부터 움직일 수 없는 경우 고려
        x, y = heapq.heappop(min_time_fish)
        board[x][y] = 0
        total_time += min_time
        fish_ate += 1
        if fish_ate == size:
            size += 1
            fish_ate = 0
    else:
        break

print(total_time)