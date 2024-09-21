# ElogV

import sys
import heapq

n = int(input())
m = int(input())
g = {i : [] for i in range(1, n+1)}
for _ in range(m):
    u, v, w = map(int, input().split())
    g[u].append((v, w))
st, en = map(int, input().split())

def dijkstra(st, en):
    h = []
    dis = {i : 10 ** 10 for i in range(1, n+1)}
    heapq.heappush(h, (0, st))
    while len(h):
        w, v = heapq.heappop(h)
        if dis[v] > w:
            dis[v] = w
            for next, next_w in g[v]:
                if dis[next] > w + next_w:
                    heapq.heappush(h, (w + next_w, next))
    return dis[en]

print(dijkstra(st, en))