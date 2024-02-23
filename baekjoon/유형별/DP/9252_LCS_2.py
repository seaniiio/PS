import sys
s1 = list(sys.stdin.readline().rstrip())
s2 = list(sys.stdin.readline().rstrip())

dp = [[''] * (len(s1)+1) for _ in range(len(s2)+1)]

for i in range(1, len(s2)+1):
    for j in range(1, len(s1)+1):
        if s2[i-1] == s1[j-1]:
            dp[i][j] = dp[i-1][j-1] + s2[i-1]
            continue
        if len(dp[i-1][j]) >= len(dp[i][j-1]):
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i][j-1]

l = dp[-1][-1]
print(len(l))
if len(l) != 0:
    print(l)

# 결과 출력 부분에서 dp[-1][-1]를 두 번 따로 사용했더니 94%에서 시간초과
# dp[-1][-1]을 한 번만 호출하도록 하자(변수에 저장)