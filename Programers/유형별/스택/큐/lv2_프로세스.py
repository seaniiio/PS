from collections import deque

def solution(priorities, location):
    answer = 1
    q = deque(priorities)
    while len(q) != 0:
        flag = True
        if max(q) > q[0]: flag = False
        if location == 0: # 알고싶은 프로세스 차례인 경우
            if not flag: # 뒤에 우선순위 높은게 있음
                q.append(q.popleft())
                location = len(q) - 1
            else: # 뒤에 우선순위 높은게 없음
                return answer
        else:
            if not flag: # 뒤에 우선순위 높은게 있음
                q.append(q.popleft())
                location = location - 1
            else: # 뒤에 우선순위 높은게 없음
                q.popleft()
                answer = answer + 1
                location = location - 1
    return answer