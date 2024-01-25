n, m = map(int, input().split())
visited = [False for _ in range(n + 1)]
G = [[0 for _ in range(n+1)] for _ in range(n+1)]
answer = 0

for _ in range(m):
    i, j = map(int, input().split())
    G[i][j], G[j][i] = 1, 1

def DFS(k):
    stk = [k]
    while stk:
        i = stk.pop()
        for j in range(1, n+1):
            if G[i][j] == 1 and visited[j] == False:
                stk.append(j)
                visited[j] = True

for i in range(1, n+1):
    if visited[i] == False:
        visited[i] = True
        DFS(i)
        answer += 1

print(answer)