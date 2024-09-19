# queue 이용

from collections import deque

def solution(sequence, k):
    answer = []
    nums = deque([])
    now = 0
    
    for i in range(len(sequence)-1, -1, -1):
        now += sequence[i]
        nums.append(sequence[i])
        while nums and now > k:
            m = nums.popleft()
            now -= m
        if now == k:
            if nums[0] == nums[-1]: # 같은 숫자만 있는 경우
                j = i
                while j-1 >= 0 and sequence[j-1] == nums[0]:
                    j -= 1
                answer = [j, j+len(nums)-1]
            else:
                answer = [i, i+len(nums)-1]
            break
    return answer