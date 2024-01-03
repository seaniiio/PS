# 물에 잠긴 지역이 리스트로 주어진다.
# 물에 잠긴 지역을 피해서 학교까지 가는 최소경로의 수는?

MAGIC_NUMBER = 1000000007

def solution(m, n, puddles):
    dp = [[0 for l in range(n+1)] for k in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if [i, j] in puddles:
                dp[i][j] = 0
            elif i == 1 and j == 1:
                dp[1][1] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]    
    print(dp)
    return dp[m][n] % MAGIC_NUMBER