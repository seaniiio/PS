# 시작 정점(1번)에서 DFS로 가장 먼 정점 구하기
# 가장 먼 정점에서 가장 먼 정점 구하기

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    v, w, d = map(int, input().split())
    graph[v].append((w, d))
    graph[w].append((v, d))


def dfs(v, total_d):
    for w, d in graph[v]:
        if visited[w] == -1:
            visited[w] = total_d + d
            dfs(w, total_d + d)
    return

visited = [-1 for _ in range(N+1)]
visited[1] = 0
dfs(1, 0)

x1 = visited.index(max(visited))
visited = [-1 for _ in range(N+1)]
visited[x1] = 0
dfs(x1, 0)

print(max(visited))
