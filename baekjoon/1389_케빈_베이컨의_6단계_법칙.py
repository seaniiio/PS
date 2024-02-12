import sys
from collections import deque

n, m = map(int, input().split())
G = {i : [] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    G[a].append(b)
    G[b].append(a)


def BFS(i):
    visited = [False for _ in range(n+1)]
    visited[i] = True
    l = [0 for _ in range(n+1)]
    q = deque([[i, 0]])
    while q:
        v, cnt = q.popleft()
        for k in G[v]:
            if visited[k] == False:
                visited[k] = True
                l[k] = cnt + 1
                q.append([k, cnt+1])
    return sum(l)

min_v = 100 * 5000
min_list = []

for i in range(1, n+1):
    k = BFS(i)
    if k == min_v:
        min_list.append(i)
    elif k < min_v:
        min_v = k
        min_list = [i]

min_list.sort()
print(min_list[0])