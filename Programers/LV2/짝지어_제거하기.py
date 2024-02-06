def solution(s):
    stk = []
    for c in s:
        if len(stk) == 0:
            stk.append(c)
        elif stk[-1] == c:
            stk.pop()
        else:
            stk.append(c)
    return int(len(stk) == 0)

# 괄호랑 비슷한 문제