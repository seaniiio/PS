# 우선순위 큐, 위상정렬
# 그래프의 진입 차수 = 해당 문제의 선행문제 개수

import sys
from queue import PriorityQueue
input = sys.stdin.readline

n, m = map(int, input().split())
G = [[] for _ in range(n+1)] # G[a] = [b, c] : b, c의 선행문제가 a
in_G = [0 for _ in range(n+1)] # 문제들에 대한 진입차수
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    in_G[b] += 1

# 진입차수가 0인, 즉 선행문제가 없는 문제들만 우선순위 큐에 삽입
pq = PriorityQueue()
for i in range(1, n+1):
    if in_G[i] == 0:
        pq.put(i)

answer = []
for i in range(n):
    k = pq.get() # 현재 풀 수 있는 문제들 중 가장 난이도가 낮은 문제
    answer.append(k)
    for v in G[k]: # 이 문제(k)가 선행인 문제들에 대해 진입차수 1 줄여주기
        in_G[v] -= 1
        if in_G[v] == 0: # 진입 차수가 0이 되면, 즉 선행 문제가 다 풀린 경우에 우선순위 큐에 삽입
            pq.put(v)

print(" ".join(map(str, answer)))