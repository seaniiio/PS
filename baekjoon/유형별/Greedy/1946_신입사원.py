import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 1
    score = []
    for _ in range(n):
        score.append(list(map(int, input().split())))
    score.sort(key=lambda x:x[0])
    min_rank = score[0][1]
    for i in range(1, n):
        if score[i][1] < min_rank:
            cnt += 1
        min_rank = min(min_rank, score[i][1])
    print(cnt)
        