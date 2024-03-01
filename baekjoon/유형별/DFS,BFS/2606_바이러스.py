from collections import deque

def DFS(stk, computers, visited, n):
    count = 1
    i = stk.pop()
    visited[i] = True
    for j in range(n):
        if computers[i][j] == 1 and i != j and visited[j] == False:
            stk.append(j)
            count += DFS(stk, computers, visited, n)
    return count

n = int(input())
m = int(input())
computers = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i == j:
            computers[i][j] = 1

for _ in range(m):
    a, b = map(int, input().split())
    computers[a-1][b-1] = 1
    computers[b-1][a-1] = 1

visited = [False for _ in range(n)]
stk = deque([0])
answer = DFS(stk, computers, visited, n)
print(answer - 1)


