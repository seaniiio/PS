def solution(nums):
    answer = 0
    l = len(nums) / 2
    nums = list(set(nums))
    if len(nums) >= l: 
        answer = l
    else:
        answer = len(nums) 
    return answer