# 프로그래머스에 비슷한 문제가 있었던 듯..?
# 수업 끝나는 시간을 기준으로 정렬
# 그냥 정렬쓰면 시간초과 날듯 -> PriorityQueue

import sys
import heapq

input = sys.stdin.readline
q = []
room = []

n = int(input())
for _ in range(n):
    heapq.heappush(q, (list(map(int, input().split())))) # 시작 시간, 끝 시간

heapq.heappush(room, heapq.heappop(q)[1])
for i in range(1, n):
    v = heapq.heappop(q)
    if room[0] <= v[0]:
        heapq.heappop(room)
        heapq.heappush(room, v[1])
    else:
        heapq.heappush(room, v[1])

print(len(room))

