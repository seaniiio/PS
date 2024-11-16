import sys
import heapq
input = sys.stdin.readline

n, m, x = map(int, input().split())
roads = {i : [] for i in range(1, n+1)}
rev_roads = {i : [] for i in range(1, n+1)}
distance = {i : 0 for i in range(1, n+1)}

for _ in range(m):
    a, b, t = map(int, input().split())
    roads[a].append([b, t])
    rev_roads[b].append([a, t])

def dijkstra(x, roads):
    global distance
    visited = {i : False for i in range(1, n+1)}
    next_nodes = [[0, x]]

    while next_nodes:
        min_dis, node = heapq.heappop(next_nodes)
        if visited[node]:
            continue

        visited[node] = True
        distance[node] += min_dis

        for n_n, d in roads[node]:
            if not visited[n_n]:
                heapq.heappush(next_nodes, [min_dis + d, n_n])

dijkstra(x, roads)
dijkstra(x, rev_roads)

print(max(distance.values()))