# 숫자로 이루어진 문자열이 주어지고, k개의 수를 제거한다고 할 때 만들 수 있는 가장 큰 수 구하기

def solution(number, k):
    length = len(number) - k
    stk = []
    idx = 0
    while idx < len(number):
        if len(stk) == 0 or k == 0:
            stk.append(number[idx])
            idx += 1
        else:
            if stk[len(stk) - 1] < number[idx]:
                stk.pop(-1)
                k -= 1
            else:
                stk.append(number[idx])
                idx += 1
    return ''.join(stk[:length])