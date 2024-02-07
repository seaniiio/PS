# 블록 채워넣는거 : 1초, 블록 빼내는거 : 2초
# 최소시간, 그때의 높이 출력
import sys

n, m, b = map(int, input().split())
l = []
for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))

high, count = -1, 256 * 500 * 501
for i in range(256, -1, -1):
    now_b = 0
    need_b = 0
    for j in range(n):
        for k in range(m):
            if l[j][k] > i:
                now_b += l[j][k] - i
            else:
                need_b += i - l[j][k]
    if now_b + b >= need_b:
        time = now_b * 2 + need_b
        if count > time:
            count = time
            high = i
        elif count == time and high < i:
            count = time
            high = i

print(count, high)