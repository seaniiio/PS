# 괄호같은 문제(stack)
from collections import deque

n = int(input())
count = 0

for i in range(n):
    stack = deque()
    s = deque(input())
    for j in range(len(s)):
        c = s.pop()
        if len(stack) == 0:
            stack.appendleft(c)
        elif stack[0] == c:
            stack.popleft()
        else:
            stack.appendleft(c)
    if len(stack) == 0:
        count += 1

print(count)
    