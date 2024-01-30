rows = [1, 0]
k = int(input())

for _ in range(k):
    n = int(input())
    dp = [[0, 0] for _ in range(n)] # [선택한 행, 누적점수]
    s = [[], []] # s[행][얄]
    for i in range(2):
        s[i] = list(map(int, input().split()))
    dp[0] = [0, s[0][0]] if (s[0][0] > s[1][0]) else [1, s[1][0]]
    answer = dp[0][1]
    if n > 1:
        if s[0][0] + s[1][1] > s[1][0] + s[0][1]:
            dp[1] = [1, s[0][0] + s[1][1]]
        else:
            dp[1] = [0, s[1][0] + s[0][1]]
        answer = max(answer, dp[1][1])
    if n > 2:
        for i in range(2, n):
            select = rows[dp[i-1][0]]
            if dp[i-1][1] + s[select][i] > dp[i-2][1] + max(s[0][i], s[1][i]): # 후보 1
                dp[i] = [select, dp[i-1][1] + s[select][i]]
            else:
                if s[0][i] > s[1][i]: # 0 선택
                    if dp[i-2][0] == 0:
                        dp[i] = [0, dp[i-2][1] + s[1][i-1] + s[0][i]]
                    else:
                        dp[i] = [0, dp[i-2][1] + s[0][i]]
                else:
                    if dp[i-2][0] == 1:
                        dp[i] = [1, dp[i-2][1] + s[0][i-1] + s[1][i]]
                    else:
                        dp[i] = [1, dp[i-2][1] + s[1][i]]
            answer = max(answer, dp[i][1])
    print(answer)
    

