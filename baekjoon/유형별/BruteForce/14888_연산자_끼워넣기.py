# eval()은 문자열로 되어있는 수식을 계산해주지만, 계속 SyntaxError를 뱉는 경우가 있으니까 그냥 쓰지 말자.

from collections import deque

n = int(input())
nums= list(map(int, input().split()))
o = list(map(int, input().split()))

max_v, min_v = -1000000000, 1000000000

def oper(now, pl, mi, mul, div, depth):
    if depth == n:
        global max_v, min_v
        max_v = max(max_v, now)
        min_v = min(min_v, now)
        return
    if pl:
        oper(now + nums[depth], pl-1, mi, mul, div, depth+1)
    if mi:
        oper(now - nums[depth], pl, mi-1, mul, div, depth+1)
    if mul:
        oper(now * nums[depth], pl, mi, mul-1, div, depth+1)
    if div:
        if now < 0:
            oper(-1 * ((-1 * now) // nums[depth]), pl, mi, mul, div-1, depth+1)
        else:
            oper(now // nums[depth], pl, mi, mul, div-1, depth+1)

oper(nums[0], o[0], o[1], o[2], o[3], 1)
print(max_v)
print(min_v)