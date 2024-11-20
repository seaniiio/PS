# 벨만 포드(one to all)
# 500 * 6000 = 3 000 000
# 시간을 무한히 오래전으로 -> 음수 순환
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
e = []
for _ in range(m):
    st, en, t = map(int, input().split())
    e.append((st, en, t))

INF = 60000000

dis = [INF] * (n+1)
neg = False

def bf(st):
    global dis, neg
    dis[st] = 0

    for i in range(n):
        for start, end, t in e:
            if dis[start] != INF and dis[end] > dis[start] + t:
                dis[end] = dis[start] + t
                if i == n-1:
                    neg = True

bf(1)

if neg:
    print(-1)
else:
    for j in range (2, n+1):
        if dis[j] == INF:
            print(-1)
        else:
            print(dis[j])