# dp[i][j] : 0...i번째 행렬 * i...j번째 행렬 -> A[i][0] * A[i][1] * A[j][0]
# dp[0][1] : A0 * A1 =  A[0][0] * A[0][1] * A[1][0]

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 9)

n = int(input())
A = []
dp = [[-1 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    i, j = map(int, input().split())
    A.append([i, j])

for i in range(n):
    dp[i][i] = 0

def Mat(i, j): # 0번째 행렬부터 n-1번째 행렬까지의 곱 수
    global dp
    for k in range(i+1, j+1): # 0~k-1번째, k~j번째로 나누기
        if dp[i][k-1] == -1:
            Mat(i, k-1)
        if dp[k][j] == -1:
            Mat(k, j)
        if dp[i][j] > 0:
            dp[i][j] = min(dp[i][j], dp[i][k-1] + dp[k][j] + A[i][0] * A[k-1][1] * A[j][1])
        else:
            dp[i][j] = dp[i][k-1] + dp[k][j] + A[i][0] * A[k-1][1] * A[j][1]

    return dp[i][j]

Mat(0, n-1)
print(dp[0][n-1])
