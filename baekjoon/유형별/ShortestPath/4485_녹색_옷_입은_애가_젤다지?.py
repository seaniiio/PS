import sys
import heapq
input = sys.stdin.readline

cnt = 1
while True:
    n = int(input())
    if n == 0:
        break
    g = []
    for _ in range(n):
        g.append(list(map(int, input().split())))
    
    h = [(g[0][0], 0, 0)]
    visited = {}
    while h:
        c, x, y= heapq.heappop(h)
        if (x, y) not in visited:
            visited[(x, y)] = c
        else:
            continue

        for dx, dy in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if 0 <= dx < n and 0 <= dy < n:
                if (dx, dy) in visited:
                    continue
                heapq.heappush(h, (c + g[dx][dy], dx, dy))
    
    print('Problem %d: %d' % (cnt, visited[(n-1, n-1)]))
    cnt += 1