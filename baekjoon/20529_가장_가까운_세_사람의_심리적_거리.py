# 비둘기집 원리 
# N > 16이면 겹치는 사람 무조건 1명 있음
# N > 32이면 겹치는 사람 무조건 2명 있음
# N > 48이면 겹치는 사람 무조건 3명 있음
# -> 시간초과 X

import sys

t = int(sys.stdin.readline())

def dist(a, b):
    cnt = 0
    for i, j in zip(a, b):
        if i != j:
            cnt += 1
    return cnt

for _ in range(t):
    n = int(sys.stdin.readline())
    mbti = list(sys.stdin.readline().split())
    answer = 0
    if n > 48:
        answer = 0
    else:
        l = []
        for i1, a in enumerate(mbti):
            for i2, b in enumerate(mbti):
                for i3, c in enumerate(mbti):
                    if i1 != i2 and i2 != i3 and i3 != i1:
                        l.append(dist(a, b) + dist(b, c) + dist(a, c))
        l.sort()
        answer = l[0]
    print(answer)