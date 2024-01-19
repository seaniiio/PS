t = int(input())

def DFS(i, j, G, m, n):
    stk = [[i, j]]
    while stk:
        v = stk.pop()
        x, y = v[0], v[1]
        G[x][y] = -1
        for dx, dy in [1, 0], [-1, 0], [0, 1], [0, -1]:
            if 0 <= x + dx < m and 0 <= y + dy < n:
                if G[x+dx][y+dy] == 1:
                    stk.append([x+dx, y+dy])


for _ in range(t):
    m, n, k = map(int, input().split())
    G = [[0 for _ in range(n)] for _ in range(m)] # G[m][n]
    count = 0
    for _ in range(k):
        x, y = map(int, input().split())
        G[x][y] = 1
    for i in range(m):
        for j in range(n):
            if G[i][j] == 1:
                DFS(i, j,G, m, n)
                count += 1
    print(count)