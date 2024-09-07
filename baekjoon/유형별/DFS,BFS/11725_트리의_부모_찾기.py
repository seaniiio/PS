# Graph 저장한 뒤, 1부터 BFS로 각 노드의 부모를 저장

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
G = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

visited = [False for _ in range(n+1)]
parents = {}

q = deque([1])
visited[1] = True
while q:
    p = q.popleft()
    for d in G[p]:
        if visited[d] == False:
            visited[d] = True
            q.append(d)
            parents[d] = p

for k in range(2, n+1):
    print(parents[k])