from collections import deque
def solution(progresses, speeds):
    q = deque(progresses)
    speeds_q = deque(speeds)
    answer = []
    while len(q) != 0:
        for i in range(len(q)):
            q[i] = q[i] + speeds_q[i]
        if q[0] >= 100:
            count = 1
            q.popleft()
            speeds_q.popleft()
            while len(q) != 0 and q[0] >= 100:
                count = count + 1
                q.popleft()
                speeds_q.popleft()
            answer.append(count)
    return answer


# 인덱스 이용
def solution(p, s):
    answer = []
    top_index = 0 # 현재(top) 인덱스
    while top_index < len(p):
        for i in range(len(p)):
            p[i] = p[i] + s[i]
        if p[top_index] >= 100:
            count = 1
            top_index = top_index + 1
            while top_index < len(p) and p[top_index] >= 100:
                count = count + 1
                top_index = top_index + 1
            answer.append(count)
    return answer