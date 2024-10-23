N = int(input())
A = list(map(int, input().split()))
dp = [-1] * (N)
dp[0] = 0

for i in range(N):
    if A[i] > 0 and dp[i] >= 0:
        for j in range(i+1, i+1+A[i]):
            if j < N:
                if dp[j] == -1:
                    dp[j] = dp[i]+1
                else:
                    dp[j] = min(dp[j], dp[i]+1)

print(dp[-1])