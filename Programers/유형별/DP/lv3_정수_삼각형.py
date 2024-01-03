# 삼각형 형태의 정수들이 주어진다.
# 이동 경로는 대각선 왼쪽 아래 혹은 대각선 오른쪽 아래이고, 이동 경로에 써있는 숫자의 합을 구한다.
# 이 숫자의 합의 최댓값은?

import math

def solution(triangle):
    dp = [arr[:] for arr in triangle]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0: # 왼쪽 모서리인 경우
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1: # 오른쪽 모서리인 경우
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    return max(dp[-1])

# 0 / 1 2 / 3 4 5 / 6 7 8 9 / 10
# 1 / 2 3 / 4 5 6 / 7 8 9 10 / 11

# dp에 현재까지의 최댓값을 저장한다.
# 대각선 위의 두 경우를 비교하여, 큰 값에 현재 값을 더해 dp에 저장한다 -> 현재까지의 최댓값이 된다.
# dp에서 최댓값을 뽑아낸다.