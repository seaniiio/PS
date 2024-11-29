# 재귀

import math

n = int(input())

result = [[' '] * (n * 2 - 1) for _ in range(n)]

def rec(level, i, j):
    global result
    if level == 1:
        result[i][j] = '*'
        result[i+1][j-1], result[i+1][j+1] = '*', '*'
        result[i+2][j-2:j+3] = '*****'
    else:
        next_h = 3 * 2 ** (level - 2)
        rec(level-1, i + next_h, j - next_h)
        rec(level-1, i, j)
        rec(level-1, i + next_h, j + next_h)

level = int(math.log2(n // 3)) + 1
rec(level, 0, (n * 2 - 1) // 2)
 
for r in result:
    print(''.join(r))