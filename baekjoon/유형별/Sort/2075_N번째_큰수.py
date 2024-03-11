# 메모리 제한이 있기 때문에, 우선순위 큐에 저장되는 원소의 개수를 n 이하로 관리하자
# N^2개의 원소를 전부 탐색하지만, 메모리를 신경써야 함
# 최소값부터 세서 모든 연산을 끝내고 남은 n개의 원소 중, 최솟값이 정답

import sys
import heapq
input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    t = list(map(int, input().split()))
    for k in t:
        if len(h) < n:
            heapq.heappush(h, k)
        else: # 이미 n개가 있을 때
            if h[0] < k: # 현재 heap의 최솟값보다 지금 넣을 숫자가 크면 heappop후 heappush
                heapq.heappop(h)
                heapq.heappush(h, k)
print(h[0])
