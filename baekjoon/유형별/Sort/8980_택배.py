# truck 배열에, 현재 실을 수 있는 무게 저장
# 도착지를 기준으로 sort -> truck 배열을 보고 실을 수 있는 만큼 싣기

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())

send = []
for _ in range(m):
    send.append(list(map(int, input().split())))
send.sort(key = lambda x: x[1])

truck = [c] * (n+1)
answer = 0
for s, d, w in send:
    can_move = min(truck[s:d])
    if can_move <= w:
        w = can_move
    for i in range(s, d):
        truck[i] -= w
    answer += w

print(answer)