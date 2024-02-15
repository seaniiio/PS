import heapq
from collections import deque

global G, visited, history
G = {}
visited = {}
history = []

def DFS(l, cnt, n):
    global G, visited, history
    if cnt == n:
        history.append(l)
        return
    before = l[-1]
    for next in G[before]:
        if next not in G.keys() and cnt == n-1:
            l.append(next)
            history.append(l)
            return
        elif next in G.keys() and visited[before, next] > 0:
            visited[(before, next)] -= 1
            new_l = l[:]
            new_l.append(next)
            result = DFS(new_l, cnt+1, n)
            if result:
                return
            visited[(before, next)] += 1

def solution(tickets):
    global G, visited, history
    n = len(tickets) + 1
    for t in tickets:
        if t[0] in G.keys():
            heapq.heappush(G[t[0]], t[1])
        else:
            G[t[0]] = [t[1]]
        if (t[0], t[1]) in visited:
            visited[(t[0], t[1])] += 1
        else:
            visited[(t[0], t[1])] = 1
    DFS(["ICN"], 1, n) # [경로], cnt
    history.sort()
    return history[0] 