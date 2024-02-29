# 결국 제곱수 개수 최대는 4이므로, 3까지만 확인해주면 된다.
# 제곱수를 저장한 리스트 nums -> 여기에 있으면 1 return
# 제곱수 두 개의 합을 저장한 리스트 nums_2 -> 여기에 있으면 2 return
# 제곱수 3개로 표현할 수 있는 경우는 nums_2의 원소 하나와 nums_1의 원소 하나를 합한 경우 -> 3 return

import math

n = int(input())
max_n = math.ceil(n ** 0.5)
nums = [k ** 2 for k in range(1, max_n+1)]
nums_2 = []
for a in nums:
    for b in nums:
        nums_2.append(a+b)

def find(n):
    global nums, nums_2
    if n in nums:
        return 1
    elif n in nums_2:
        return 2
    for k in nums_2:
        if n - k in nums:
            return 3
    return 4

print(find(n))