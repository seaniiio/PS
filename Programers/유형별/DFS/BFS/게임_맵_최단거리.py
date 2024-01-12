from collections import deque

def BFS(maps, v):
    q = deque([v])
    y_max = len(maps) - 1
    x_max = len(maps[0]) - 1
    visited = [[0 for i in range(x_max + 1)] for j in range(y_max + 1)]
    visited[0][0] = 1

    while q:
        now = q.popleft() # (0,0,1)
        if now[0] == y_max and now[1] == x_max:
            return now[2]
        for d in (1,0), (-1,0), (0,1), (0,-1):
            ny, nx = now[0] + d[0], now[1] + d[1]
            if 0 <= ny <= y_max and 0 <= nx <= x_max and visited[ny][nx] == 0 and maps[ny][nx] == 1:
                q.append((ny, nx, now[2]+1))
                visited[ny][nx] = 1
    return -1

def solution(maps):
    return BFS(maps, (0, 0, 1))


# 갈 수 있는 경로는 상, 하, 좌, 우 4가지.
# 처음에 이 경로 하나하나 if문 세워서 총 4개의 if문으로 지저분하게 만들었었다.
# 근데 for문으로 한 번에 돌릴 수 있다는 것을 알게 되고 길이가 엄청 짧아짐
# visited 리스트를 만들어서 visited한 좌표를 튜플로 넣고, if ~~ in visited 했었는데 시간초과 났다.
# 추후에 다시 한 번 풀어볼만한 문제.

# for문으로 4가지 경우 전부 계산하기, BFS에서 visited 체크는 pop할때 하는 것이 아니라 append할 때 해주기(효율성), for문 안에서도 ny nx로 계산을 해두고 조건문 짜면 훨씬 보기 편함!