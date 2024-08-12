# 간격이 테이프 길이보다 작으면 이어붙이기

n, tape_l = map(int, input().split())
pipe = list(map(int, input().split()))

pipe.sort()
cnt = 1
now, next = 0, 1

while next < len(pipe):
    if pipe[next] - pipe[now] <= tape_l - 1:
        next += 1
    else:
        cnt += 1
        now = next
        next += 1

print(cnt)