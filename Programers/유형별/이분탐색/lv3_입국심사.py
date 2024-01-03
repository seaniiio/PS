# n명이 입국심사를 받기위해 기다리고 있다.
# 각 심사관의 심사 소요시간이 list로 주어진다.
# 모두가 심사받기 위해 필요한 최소한의 시간은?

# target값: 시간

def solution(n, times):
    answer = 0
    times.sort()
    left = 1
    right = times[-1] * n
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for time in times:
            people += (mid // time)
            if people >= n: # 심사 완료한 사람이 n보다 크거나 같을 때
                break
        if people >= n: # 너무 많이 검사 -> time 기준을 줄여도 됨
            right = mid - 1
            answer = mid
        else: # 너무 적게 검사 -> time 기준을 키워도 됨
            left = mid + 1
    return answer


# 이분탐색 언제 사용?
# 1. 입력값의 범위가 엄청 클 때, 입력값이 엄청 많을 때
# 2. target값이 명확하게 존재할 때

# 이분탐색 어떻게 사용?
# 1. target에 대한 left, right 설정
# 2. while -> for -> if-break 구조
# 3. 기준(이 문제에서는 사람 수, people)보다 작은지 큰지 판단해서, left와 right를 조정