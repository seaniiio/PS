# X로부터 모든 마을까지의 최소경로 -> SSSP -> Dijkstra
import heapq
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
g = {i:[] for i in range(1, n+1)}
for _ in range(m):
    v, w = map(int, input().split())
    g[v].append(w)

visited = {i : -1 for i in range(1, n+1)}
def dijkstra(x):
    global visited
    h = []
    heapq.heappush(h, (0, x))
    while len(h):
        d, v = heapq.heappop(h)
        if visited[v] == -1:
            visited[v] = d
            for w in g[v]:
                if visited[w] == -1:
                    heapq.heappush(h, (d+1, w))

dijkstra(x)
answer = []
for key, value in visited.items():
    if value == k:
        answer.append(key)

answer.sort()
if len(answer) == 0:
    print(-1)
else:
    for a in answer:
        print(a)