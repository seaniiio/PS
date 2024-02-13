import sys
import heapq

n = int(input())
h = []
for _ in range(n):
    k = int(sys.stdin.readline())
    if k == 0:
        if len(h) == 0:
            print(0)
        else:
            print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h, [-k, k])