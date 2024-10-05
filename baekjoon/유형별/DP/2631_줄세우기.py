# 증가하는 가장 긴 부분수열 길이를 전체 길이에서 빼주면 될듯

n = int(input())
kids = []
for _ in range(n):
    kids.append(int(input()))

dp = [1] * n
for i in range(n):
    for j in range(i, n):
        if kids[i] < kids[j]:
            dp[j] = max(dp[j], dp[i] + 1)

print(n - max(dp))