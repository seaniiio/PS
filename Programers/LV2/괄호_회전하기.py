# 완전 탐색
# dict 이용하면 조건문 3개 쓸 걸 하나로 줄일 수 있다.

from collections import deque

dict = {')' : '(', ']' : '[', '}' : '{'}

def is_right(s):
    stk = []
    for k in s:
        if len(stk) == 0:
            if k == '(' or k == '[' or k == '{': stk.append(k)
            else: return False
        else:
            if k in dict.keys():
                if dict[k] == stk[-1]:
                    stk.pop()
            else:
                stk.append(k)
    if len(stk) == 0:
        return True
    else:
        return False
    
def solution(s):
    s = deque(s)
    cnt = 0
    for i in range(len(s)):
        s.append(s.popleft())
        if is_right(s):
            cnt += 1
    return cnt