# 힙도 익셔너리인가?

import sys
import heapq

h = []
n = int(input())
for _ in range(n):
    k = int(sys.stdin.readline())
    if k == 0:
        if len(h) == 0:
            print(0)
        else:
            print(heapq.heappop(h))
    else:
        heapq.heappush(h, k)