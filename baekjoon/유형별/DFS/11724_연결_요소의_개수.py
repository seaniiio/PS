import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
visited = [False for _ in range(n + 1)]
G = [[] for _ in range(n+1)]
answer = 0

for _ in range(m):
    i, j = map(int, input().split())
    G[i].append(j)
    G[j].append(i)

def DFS(k):
    stk = deque([k])
    while stk:
        i = stk.pop()
        for j in G[i]:
            if visited[j] == False:
                visited[j] = True
                stk.append(j)

for i in range(1, n+1):
    if visited[i] == False:
        visited[i] = True
        DFS(i)
        answer += 1

print(answer)