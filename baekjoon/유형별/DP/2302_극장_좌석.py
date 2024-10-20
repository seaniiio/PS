# 한 좌석에 앉을 수 있는 사람의 경우의 수는 최대 3
# 40자리
# 3^40 -> 시간초과
# DP

N = int(input())
M = int(input())
vip = []
for _ in range(M):
    vip.append(int(input()))

dp = [0] * (N+1)
dp[0], dp[1] = 1, 1

for i in range(2, N+1):
    if i in vip:
        dp[i] = dp[i-1]
    else:
        if i-1 in vip:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1] + dp[i-2]
print(dp[-1])