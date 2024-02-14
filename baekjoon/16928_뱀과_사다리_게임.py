from collections import deque

n, m = map(int, input().split())
G = [i for i in range(101)]

for _ in range(n + m):
    a, b = map(int, input().split())
    G[a] = b

cnt_min = 100
q = deque([[1, 0]]) # 현재 칸, cnt
visited = [False for _ in range(101)]
while q:
    now, cnt = q.popleft()
    if now >= 100:
        cnt_min = min(cnt, cnt_min)
    for i in range(1, 7):
        if now + i <= 100:
            if visited[now + i] == False:
                visited[now + i] = True
                q.append([G[now+i], cnt+1])

print(cnt_min)
