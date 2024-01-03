# 음식들의 스코빌 지수가 담긴 list가 주어진다.
# 모든 음식의 스코빌지수가 K 이상이 되도록 해야 한다.
# `섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)`
# 만약 모든 음식의 스코빌 지수를 K 이상으로 만들지 못할 경우 -1을 return

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K and len(scoville) >= 2: # 원소가 1개일 때 두 번 pop할수 없기 때문에 while 탈출
        answer = answer + 1
        new_scoville = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, new_scoville)
    if scoville[0] < K: # while을 탈출했는데 모든 음식의 스코빌 지수가 k이상이 아닌 경우
        return -1 
    return answer