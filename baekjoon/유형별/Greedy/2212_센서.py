# 전체 거리(첫 센서 ~ 마지막 센서)에서, 센서가 없는 간격이 긴 부분들만큼 빼주기

import sys

input = sys.stdin.readline
n = int(input())
m = int(input())

sensors = list(map(int, input().strip().split()))
sensors.sort()
max_distance = sensors[-1] - sensors[0]

distances = [sensors[i+1] - sensors[i] for i in range(len(sensors) - 1) if sensors[i+1] != sensors[i]]
distances.sort(reverse = True)
dis_idx = 0

for _ in range(m-1):
    if dis_idx < len(distances):
        max_distance -= distances[dis_idx]
        dis_idx += 1

print(max_distance)