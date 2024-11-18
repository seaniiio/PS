import heapq

n, k = map(int, input().split())
visited = {i:100001 for i in range(0, 100001)}
q = [(0, k)]
visited[k] = 0
ans = -1

while q:
    t, now = heapq.heappop(q)
    if now == n:
        ans = t
        break

    if now % 2 == 0:
        if 0 < now and t < visited[now // 2]:
            heapq.heappush(q, (t, now // 2))
            visited[now // 2] = t
    for next in (now-1, now+1):
        if 0 <= next <= 100000 and t+1 < visited[next]:
            heapq.heappush(q, (t+1, next))
            visited[next] = t+1

print(ans)