import sys
from collections import deque

n = int(input())
G = {i : [] for i in range(n)}
for i in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    for idx, k in enumerate(l):
        if k == 1:
            G[i].append(idx)

def BFS(i):
    q = deque([i])
    visited = [0] * n
    while q:
        v = q.popleft()
        for k in G[v]:
            if visited[k] == 0:
                visited[k] = 1
                q.append(k)
    print(*visited)

for i in range(n):
    BFS(i)