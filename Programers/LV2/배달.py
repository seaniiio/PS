# 다익스트라
import heapq

def solution(N, road, K):
    graph = {i:[] for i in range(1, N+1)}
    for v, w, weight in road:
        graph[v].append((w, weight))
        graph[w].append((v, weight))
    
    pq = []
    answer = [1]
    visited = {i : 500001 for i in range(1, N+1)}
    visited[1] = -1
    
    for ad in graph[1]:
        heapq.heappush(pq, (ad[0], ad[1]))
        
    while pq:
        w, total_w = heapq.heappop(pq)
        if total_w <= K:
            answer.append(w)
            for ad in graph[w]:
                if visited[ad[0]] > ad[1] + total_w:
                    heapq.heappush(pq, (ad[0], ad[1]+total_w))
                    visited[ad[0]] = ad[1] + total_w
    return len(set(answer))