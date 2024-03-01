from collections import deque

n, m, v = map(int, input().split())
G = [[] for _ in range(0, n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

def DFS(v, G):
    visited = []
    stk = [v]
    while len(stk) != 0:
        now = stk.pop()
        if now not in visited:
            visited.append(now)
            temp = []
            for i in G[now]:
                if i not in visited:
                    temp.append(i)
            temp.sort(reverse = True)
            stk.extend(temp)
    print(' '.join(str(x) for x in visited))

def BFS(v, G):
    visited = []
    queue = deque([v])
    while len(queue) != 0:
        now = queue.popleft()
        if now not in visited:
            visited.append(now)
            temp = []
            for i in G[now]:
                if i not in visited:
                    temp.append(i)
            temp.sort(reverse = False)
            queue += temp
    print(' '.join(str(x) for x in visited))

DFS(v, G)
BFS(v, G)