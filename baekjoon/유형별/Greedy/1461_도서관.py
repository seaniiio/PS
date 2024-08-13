# 먼 곳을 최소한으로 가야함
# -끼리, +끼리 같이 들기
# 최대값 필요 -> heapq
# 마지막 갖다놓는 책은 돌아오지 않아도 됨 -> 절댓값 최대인 거리 하나 구하기

import heapq

pq_plus, pq_minus = [], [] # maxheap
n, m = map(int, input().split())

arr = list(map(int, input().split()))
abs_arr = list(map(abs, arr))
max_d = max(abs_arr)

for i in range(n):
    if arr[i] > 0:
        heapq.heappush(pq_plus, -arr[i])
    else:
        heapq.heappush(pq_minus, arr[i])

total_move = 0
books = 1 # 현재 들고있는 책 수
while len(pq_plus) != 0:
    move = -heapq.heappop(pq_plus)

    while books < m:
        if len(pq_plus) != 0:
            heapq.heappop(pq_plus)
        books += 1
    total_move += move * 2
    books = 1

while len(pq_minus) != 0:
    move = -heapq.heappop(pq_minus)

    while books < m:
        if len(pq_minus) != 0:
            heapq.heappop(pq_minus)
        books += 1
    total_move += move * 2
    books = 1

total_move -= max_d
print(total_move)