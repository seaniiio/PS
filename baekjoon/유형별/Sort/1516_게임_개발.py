# 위상정렬
# 꼭다시풀어보자~

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
build = {i : [] for i in range(1, n+1)}
indegree = {i : 0 for i in range(1, n+1)}
time = {i : 0 for i in range(1, n+1)}
for j in range(n):
    inputs = list(map(int, input().split()))
    for i, k in enumerate(inputs):
        if i == 0:
            time[j+1] = k
        elif k != -1:
            build[k].append(j+1)
            indegree[j+1] += 1

answer = {i : 0 for i in range(1, n+1)}
q = deque([])
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        answer[i] = time[i]

while q:
    v = q.popleft()

    for b in build[v]:
        indegree[b] -= 1
        answer[b] = max(answer[b], answer[v] + time[b])
        if indegree[b] == 0:
            q.append(b)

for i in range(1, n+1):
    print(answer[i])