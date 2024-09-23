# 중복으로 담는거 방지하려면, 무게 큰 것부터 담기

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
bag = []
dp = {i : 0 for i in range(k+1)}
for _ in range(n):
    w, v = map(int, input().split())
    if w not in dp:
        dp[w] = 0
    bag.append((w, v))

bag.sort(key = lambda x:-x[0])
for w, v in bag:
    for u in range(k, w-1, -1):
        dp[u] = max(dp[u], v + dp[u-w])

print(dp[k])