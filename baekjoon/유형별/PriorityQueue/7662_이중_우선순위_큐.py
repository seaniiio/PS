# 최솟값, 최댓값을 뺄 때 각각 min-heap, max-heap 이용
# 결국 숫자들에 대한 정보를 하나로 관리해야 하기 때문에 nums라는 딕셔너리 이용
# pop연산을 하면 해당 num에 대해 value를 -1 해줌
# value가 0이면 이미 그 숫자가 없다는 의미이므로 nums에서 del해줌

import sys
import heapq

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    min_q = []
    max_q = []
    nums = {}

    for _ in range(n):
        s = list(input().split())
        s[1] = int(s[1])
        if s[0] == 'I':
            heapq.heappush(min_q, s[1])
            heapq.heappush(max_q, (-s[1], s[1]))
            if s[1] in nums:
                nums[s[1]] += 1
            else:
                nums[s[1]] = 1
        elif s[0] == 'D':
            if len(nums.keys()) != 0:
                k = 0
                if s[1] == -1:
                    while True:
                        k = heapq.heappop(min_q)
                        if k in nums.keys():
                            break
                else: 
                    while True:
                        k = heapq.heappop(max_q)[1]
                        if k in nums.keys():
                            break
                nums[k] -= 1
                if nums[k] == 0:
                    del(nums[k])

    if len(nums.keys()) == 0:
        print("EMPTY")
    else:
        print(max(nums.keys()), min(nums.keys()))