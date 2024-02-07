import sys

n = int(input())
l = [[0, 0]]
dp = [0] * 16
for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n+1):
    m = 0
    for j in range(0, i):
        if i - j >= l[j][0]:
            if n - i >= l[i][0] - 1:
                m = max(m, l[i][1] + dp[j])
        
    dp[i] = m
print(max(dp))