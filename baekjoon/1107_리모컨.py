import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
button = [i for i in range(10)]
x_button = []
if m != 0:
    x_button = list(map(int, input().split()))
button = list(set(button) - set(x_button))
def ten(k): # 자릿수
    if k == 0:
        return 1
    cnt = 0
    while k > 0:
        k //= 10
        cnt += 1
    return cnt

result = abs(100 - n)
n_ten = ten(n)

def dfs(now, now_ten):
    global result
    result = min(result, abs(now - n) + now_ten)
    if now_ten == 6:
        return
    for b in button:
        dfs(now * 10 + b, now_ten + 1)

for k in button:
    dfs(k, 1)

print(result)