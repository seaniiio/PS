import sys
input = sys.stdin.readline

n = int(input())
times = []
for _ in range(n):
    times.append(list(map(int, input().split())))

times.sort(key = lambda x : (x[1], x[0]))
now_time = 0
cnt = 0
for t in times:
    if t[0] >= now_time:
        now_time = t[1]
        cnt += 1
print(cnt)