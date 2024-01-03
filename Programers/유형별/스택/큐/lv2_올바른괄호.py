def solution(s):
    answer = True
    stk = []
    for c in s:
        if len(stk) == 0:
            stk.append(c)
        elif c == ')' and stk[-1] == '(': # 짝이 맞는 경우
            stk.pop()
        else:
            stk.append(c)
    if len(stk) != 0 : answer = False
    return answer

