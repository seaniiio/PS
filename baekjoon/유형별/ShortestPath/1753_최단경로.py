import sys
import heapq

input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())

graph = {i : [] for i in range(1, V+1)}
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

visited = {i : 3000001 for i in range(1, V+1)}
def dijkstra(x):
    global visited
    h = [(0, x)]
    while len(h):
        w, v = heapq.heappop(h)
        if w < visited[v]:
            visited[v] = w
            for next, next_w in graph[v]:
                if visited[next] > w + next_w:
                    heapq.heappush(h, (w+next_w, next))

dijkstra(K)

for d in visited.values():
    if d == 3000001:
        print("INF")
    else:
        print(d)