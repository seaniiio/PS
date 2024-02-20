# 두 큐의 sum을 비교해서, sum이 큰 큐에서 sum이 작은 큐로 숫자 이동
# 답이 나올 수 있는 반복 횟수를 넘어가면, 답을 못 찾는 것으로 해서 -1 return

from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    while True:
        new_sum1, new_sum2 = 0, 0
        if sum1 == sum2:
            break
        elif sum1 < sum2:
            k = q2.popleft()
            q1.append(k)
            new_sum1 = sum1 + k
            new_sum2 = sum2 - k
        elif sum1 > sum2:
            k = q1.popleft()
            q2.append(k)
            new_sum2 = sum2 + k
            new_sum1 = sum1 - k
        sum1 = new_sum1
        sum2 = new_sum2
        answer += 1
        if answer > 300000:
            return -1
    return answer