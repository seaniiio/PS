# 이게 stack을 이용한 대표적 문제임을 잊지 말자

import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
nge = [-1 for _ in range(n)]
stk = []

for i, value in enumerate(l):
    while len(stk) > 0 and stk[-1][0] < value:
        pop_v, pop_i = stk.pop()
        nge[pop_i] = value
    stk.append([value, i])

print(' '.join(list(map(str, nge))))