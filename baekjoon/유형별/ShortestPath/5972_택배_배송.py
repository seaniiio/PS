import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
g = {i : [] for i in range(1, n+1)}

for _ in range(m):
    v, w, c = map(int, input().split())
    g[v].append((w, c))
    g[w].append((v, c))

def dijkstra(st, en):
    visited = {i : False for i in range(1, n+1)}
    h = [(0, st)]
    while h:
        c, now = heapq.heappop(h)
        if visited[now] == False:
            visited[now] = True
            if now == en:
                return c
            for next, next_c in g[now]:
                if visited[next] == False:
                    heapq.heappush(h, (c + next_c, next))

print(dijkstra(1, n))