# 마감일을 기준으로, 맨 뒤 마감일부터 생각
# 그 당시에 제출할 수 있는(마감기한이 지나지 않은) 과제들 중 점수가 가장 높은 과제 수행 -> PQ

import heapq

pq = []
n = int(input())
assignments = []
for _ in range(n):
    assignments.append(tuple(map(int, input().split())))

assignments.sort(key = lambda x : x[0], reverse=True)
now_day = assignments[0][0] # 현재 마감일

answer = 0
while now_day > 0:
    for i in range(n):
        if assignments[i][0] == now_day:
            heapq.heappush(pq, (-1) * assignments[i][1])
        elif assignments[i][0] < now_day:
            break
    
    if len(pq) != 0:
        answer += (-1) * heapq.heappop(pq)
    now_day -= 1
    
print(answer)