# st -> v1 -> v2 -> en
# st -> v2 -> v1 -> en
# 중 최단 경로 구하기 (dijkstra 6번)

import sys
import heapq
input = sys.stdin.readline

N, E = map(int, input().split())
g = {i : [] for i in range(1, N+1)}
for _ in range(E):
    u, v, t = map(int, input().split())
    g[u].append((v, t))
    g[v].append((u, t))

def dijkstra(st, en):
    visited = {i : False for i in range(1, N+1)}
    visited[st] = True
    h = [(0, st)]

    while h:
        now_t, now_v = heapq.heappop(h)
        if now_v == en:
            return now_t
        visited[now_v] = True
        for next, t in g[now_v]:
            if visited[next] == False:
                heapq.heappush(h, (now_t+t, next))
    
    return -1

v1, v2 = map(int, input().split())
INF = 6 * (10 ** 8)
ans_1, ans_2 = INF, INF

st_to_v1, v1_to_v2, v2_to_en = dijkstra(1, v1), dijkstra(v1, v2), dijkstra(v2, N)
if -1 not in (st_to_v1, v1_to_v2, v2_to_en):
    ans_1 = st_to_v1 + v1_to_v2 + v2_to_en

st_to_v2, v2_to_v1, v1_to_en = dijkstra(1, v2), dijkstra(v2, v1), dijkstra(v1, N)
if -1 not in (st_to_v2, v2_to_v1, v1_to_en):
    ans_2 = st_to_v2 + v2_to_v1 + v1_to_en

ans = min(ans_1, ans_2)
if ans == INF:
    print(-1)
else:
    print(ans)