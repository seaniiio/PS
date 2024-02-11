import heapq
import sys

n = int(input())
h = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x:
        l = (-x if x < 0 else x, x)
        heapq.heappush(h, l)
    else:
        if len(h) == 0:
            print(0)
        else:
            print(heapq.heappop(h)[1])