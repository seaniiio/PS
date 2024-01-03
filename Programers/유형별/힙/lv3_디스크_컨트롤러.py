# 각 작업에 대해 [요청시점, 소요시간]을 담은 리스트가 존재하고, 이 리스트들을 담은 리스트가 주어진다.
# 모든 작업에 대해 요청부터 걸린 시간의 평균을 구해서 return한다.

import heapq

def solution(jobs):
    answer = 0
    now_time = 0 # 이전 작업이 끝난 시간
    start_time = -1 # 이전 작업이 시작된 시간
    sum_time = 0
    minHeap = []
    for j in jobs: # 종료조건을 위한 모든 job의 time sum 계산ㄴ
        sum_time = sum_time + j[1]
    while now_time < sum_time:
        for j in jobs:
            if start_time < j[0] <= now_time: # 조건이 이렇게 들어가는 이유는, 이전에 push하지 않았던 것들중 새롭게 push할 수 있는것만 뽑아내기 위해서
                heapq.heappush(minHeap, (j[1], j[0])) # 걸리는 시간을 기준으로 min값을 구해야 함 -> 순서 뒤집음
        if minHeap:
            now_job = heapq.heappop(minHeap)
            # start time과 now time 업데이트
            start_time = now_time
            now_time += now_job[0]
            answer += (now_time - now_job[1]) # 요청으로부터 소요된 시간
        else:
            now_time += 1 # 작업할 수 있는 것이 없는 경우
    return answer // len(jobs)