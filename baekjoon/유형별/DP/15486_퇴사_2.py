import sys
input = sys.stdin.readline

N = int(input())
T, P = [0], [0]
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
dp = [0] * (N+2)

now_max = 0
for i in range(1, N+1):
    if i + T[i] <= N+1:
        if dp[i] > now_max:
            now_max = dp[i]
        dp[i + T[i]] = max(now_max + P[i], dp[i + T[i]])
    if dp[i] > now_max:
        now_max = dp[i]

print(max(dp))