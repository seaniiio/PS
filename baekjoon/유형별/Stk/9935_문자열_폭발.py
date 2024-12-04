# kmp

from collections import deque

s = list(input())
bomb_s = list(input())
bomb_len = len(bomb_s)
ans = []

for i in range(len(s)):
    ans.append(s[i])
    is_same = True
    for j in range(bomb_len):
        if len(ans) <= j or ans[-1-j] != bomb_s[bomb_len-1-j]:
            is_same = False
            break
    if is_same:
        for _ in range(bomb_len):
            ans.pop()
        continue

if len(ans) == 0:
    print("FRULA")
else:
    print(''.join(ans))