import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

V = int(input())
G = [[] for _ in range(V+1)]

for _ in range(V):
    I = list(map(int, input().split()))
    v = I[0]
    i = 1
    while I[i] != -1:
        w, b = I[i], I[i+1]
        G[v].append((w, b))
        i += 2

def DFS(st, v):
    global visited
    visited[st] = v
    for w, d in G[st]:
        if visited[w] == -1:
            DFS(w, v+d)
    return

visited = [-1 for _ in range(V+1)]
DFS(1, 0)
x1 = visited.index(max(visited))
        
visited = [-1 for _ in range(V+1)]
DFS(x1, 0)
print(max(visited))