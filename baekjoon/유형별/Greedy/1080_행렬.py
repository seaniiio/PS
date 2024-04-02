# 문제 이해가 어려웠음
# 뒤집는 연산은 무조건 3x3으로만 일어날 수 있음
# 행렬의 첫 원소부터 돌면서, 뒤집어야 하면 뒤집기연산 하고, 총 연산횟수 print

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = []
b = []
for _ in range(n):
    a.append(list(map(int, input().strip())))
for _ in range(n):
    b.append(list(map(int, input().strip())))

def change(x, y):
    global a
    for i in range(x, x+3):
        for j in range(y, y+3):
            if a[i][j] == 1:
                a[i][j] = 0
            else:
                a[i][j] = 1

cnt = 0
if n < 3 or m < 3:
    print(-1)
else:
    for i in range(n-2):
        for j in range(m-2):
            if a[i][j] != b[i][j]:
                change(i, j)
                cnt += 1
    if a != b:
        cnt = -1
    print(cnt)
