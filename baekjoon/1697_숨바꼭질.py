from collections import deque

n, k = map(int, input().split())

def F(n):
    cnt = 1
    q = deque([[0, n]])
    visited = [False] * 1000001
    visited[n] = True
    while q:
        V = q.popleft()
        v = V[1]
        cnt = V[0]
        if v == k:
            print(cnt)
            return
        for now in v-1, v+1, v*2:
            if 0 <= now <= 100000 and visited[now] == False:
                visited[now] = True
                q.append([cnt + 1, now])
F(n)