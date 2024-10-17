# dp[k][cnt] : k초에 cnt번 자리를 바꿔서 먹은 최대 자두의 수

import sys
input = sys.stdin.readline

T, W = map(int, input().split())
tree = [0]
for _ in range(T):
    tree.append(int(input()))

now_tree = 1
dp = [[0] * (W+1) for _ in range(T+1)]

for i, t in enumerate(tree):
    if i == 0:
        continue

    dp[i][0] = dp[i-1][0] + (t % 2)
    for w in range(1, W+1):
        # 먹은 경우
        if t == (w % 2) + 1:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-1]) + 1
        # 먹지 않은 경우
        else:
            dp[i][w] = max(dp[i-1][w-1], dp[i-1][w])

print(max(dp[-1]))