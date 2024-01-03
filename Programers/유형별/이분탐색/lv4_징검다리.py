# 출발지점과 도착지점 사이에 바위들이 존재
# 이 바위들 중 n개를 제거하는데, 지점들과 바위들 사이의 거리 중 최솟값이 최대가 되도록 제거해야 함

# target값: 거리

def solution(distance, rocks, n):
    answer = 0
    left = 1
    right = distance
    rocks.sort()
    rocks.append(distance)
    while left <= right:
        mid = (left + right) // 2
        before_rock = 0
        remove_rock = 0
        for rock in rocks:
            if rock - before_rock < mid: # 기준이 되는 distance보다 거리가 작은 경우
                remove_rock += 1 # 돌을 제거
                if remove_rock > n:
                    break
            else:
                before_rock = rock
        if remove_rock > n: # remove한 돌 개수가 너무 많은 경우 -> 기준치 distance를 낮춰야 함
            right = mid - 1 # 기준이 더 빡쎄짐
        else: # remove한 돌 개수가 적절하거나 적은 경우 -> 기준치 distance를 높여야 함
            answer = mid
            left = mid + 1 # 기준이 널널해짐
    return answer

# 이분탐색 언제 사용?
# 1. 입력값의 범위가 엄청 클 때, 입력값이 엄청 많을 때
# 2. target값이 명확하게 존재할 때

# 이분탐색 어떻게 사용?
# 1. target에 대한 left, right 설정
# 2. while -> for -> if-break 구조
# 3. 기준(이 문제에서는 제거한 돌 개수, remove_rock)보다 작은지 큰지 판단해서, left와 right를 조정