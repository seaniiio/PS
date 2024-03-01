# 오큰수에서 비교하는 기준이 cnt로 바뀐 것

import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
cnt = [0 for _ in range(1000001)]
for k in l:
    cnt[k] += 1

stk = []
ngf = [-1 for _ in range(n)]
for i, value in enumerate(l):
    now_ngf = cnt[value]
    while len(stk) > 0 and stk[-1][0] < now_ngf:
        k, idx = stk.pop()
        ngf[idx] = value
    stk.append([cnt[value], i])

print(' '.join(list(map(str, ngf))))