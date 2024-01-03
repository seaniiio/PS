# 입력, 최댓값 삭제, 최솟값 삭제 연산이 존재하는 자료구조를 구현하는 문제
# 모든 명령어를 수행하고 [최댓값, 최솟값]을 return

#1 시간초과 날 줄 알았는데 안 난 풀이..

import heapq

heap = []

def solution(operations):
    answer = [0, 0]
    for o in operations:
        if o[0] == 'I': # push 연산
            I, num = o.split(" ")
            heapq.heappush(heap, int(num))
        elif o == "D -1": # 최솟값 삭제 연산
            if heap:
                heapq.heappop(heap) # min heap이니까 그냥 최솟값 제거
        elif o == "D 1": # 최댓값 삭제 연산
            if heap:
                heap.remove(max(heap)) # 최댓값 remove
                heapq.heapify(heap) # heappop이 아니라 remove를 했으니까 heap구조 깨짐 -> heapify 해줘야 함

    if heap:
        answer[1] = heapq.heappop(heap)
        answer[0] = max(heap)
    return answer


#2 처음에 시간 고려해서 생각한 풀이
# min heap에서 최댓값은 tree의 마지막 depth에 무조건 있다는 성질 이용

import heapq
import math

heap = []

def solution(operations):
    answer = [0, 0]
    for o in operations:
        if o[0] == 'I':
            I, num = o.split(" ")
            heapq.heappush(heap, int(num))
        elif o == "D -1":
            if heap:
                heapq.heappop(heap)
        elif o == "D 1":
            if heap:
                max = findMax(heap)
                heap.remove(max)
                heapq.heapify(heap)
    if heap:
        answer[1] = heapq.heappop(heap)
        answer[0] = findMax(heap)
    return answer

def findMax(heap): # heap의 마지막 depth에서 최댓값 구하기
    max = heap[0]
    l = len(heap)
    length_log = int(math.log2(l))
    n = 2 ** length_log
    for i in range(l-n, l):
        if heap[i] > max:
            max = heap[i]
    return max
